from typing import List, Dict, Any, Optional
import httpx
from app.domain.external.llm import LLM
from app.core.config import get_settings
import logging
import json


logger = logging.getLogger(__name__)

class N8nLLM(LLM):
    def __init__(self):
        settings = get_settings()
        self.webhook_url = settings.n8n_webhook_url
        
        # Automatically use production webhook if test webhook is configured
        if "/webhook-test/" in self.webhook_url:
            original_url = self.webhook_url
            self.webhook_url = self.webhook_url.replace("/webhook-test/", "/webhook/")
            logger.warning(f"Converted test webhook URL to production: {original_url} -> {self.webhook_url}")
        
        # Optional fallback webhook (e.g., switch from /webhook-test/ to /webhook/ or use local mockserver)
        self.fallback_webhook_url: Optional[str] = getattr(settings, "n8n_fallback_webhook_url", None)
        
        self._model_name = "n8n-workflow"
        self._temperature = 0.7
        self._max_tokens = 2000
        logger.info(f"Initialized N8n LLM with webhook: {self.webhook_url}")
    
    @property
    def model_name(self) -> str:
        return self._model_name
    
    @property
    def temperature(self) -> float:
        return self._temperature
    
    @property
    def max_tokens(self) -> int:
        return self._max_tokens
    
    async def ask(self, messages: List[Dict[str, str]],
                  tools: Optional[List[Dict[str, Any]]] = None,
                  response_format: Optional[Dict[str, Any]] = None,
                  tool_choice: Optional[str] = None) -> Dict[str, Any]:
        """Send chat request to n8n workflow with full history."""
        try:
            # Last user message
            user_message = ""
            for msg in reversed(messages):
                if msg.get("role") == "user":
                    user_message = msg.get("content", "")
                    break

            # Include entire history for context preservation
            safe_history: List[Dict[str, str]] = []
            for m in messages:
                role = m.get("role")
                content = m.get("content", "")
                if role in ("user", "assistant", "system"):
                    safe_history.append({"role": role, "content": content})

            payload: Dict[str, Any] = {
                "input": user_message,
                "sessionId": "default_session",  # TODO: pass real session id when available
                "history": safe_history,
            }

            logger.debug(f"Sending request to n8n workflow: {payload}")

            async with httpx.AsyncClient(timeout=120.0) as client:
                try:
                    response = await client.post(
                        self.webhook_url,
                        json=payload,
                        headers={"Content-Type": "application/json"}
                    )
                    response.raise_for_status()
                except httpx.TimeoutException as timeout_err:
                    logger.error(f"Timeout calling n8n webhook (120s): {str(timeout_err)}")
                    raise Exception(f"n8n workflow timeout after 120 seconds. The workflow may be processing a complex request or the service may be slow.") from timeout_err
                except httpx.ConnectError as conn_err:
                    logger.error(f"Connection error calling n8n webhook: {str(conn_err)}")
                    raise Exception(f"Failed to connect to n8n workflow at {self.webhook_url}. Please check if the n8n service is running and accessible.") from conn_err
                except httpx.HTTPStatusError as http_err:
                    status = http_err.response.status_code if http_err.response is not None else None
                    # If test webhook is 404, try production path automatically
                    if status == 404 and "/webhook-test/" in self.webhook_url:
                        prod_url = self.webhook_url.replace("/webhook-test/", "/webhook/")
                        logger.warning(f"n8n test webhook returned 404. Retrying with production webhook: {prod_url}")
                        response = await client.post(
                            prod_url,
                            json=payload,
                            headers={"Content-Type": "application/json"}
                        )
                        response.raise_for_status()
                    # If still failing (or different 4xx/5xx), try explicit fallback webhook when configured
                    elif status in (404, 410) and self.fallback_webhook_url:
                        logger.warning(f"n8n webhook returned {status}. Retrying with fallback webhook: {self.fallback_webhook_url}")
                        response = await client.post(
                            self.fallback_webhook_url,
                            json=payload,
                            headers={"Content-Type": "application/json"}
                        )
                        response.raise_for_status()
                    else:
                        raise

                # Try to parse JSON response (array of objects with `output`), else use raw text
                content: str
                try:
                    data = response.json()
                    if isinstance(data, list) and data and isinstance(data[0], dict) and "output" in data[0]:
                        content = str(data[0]["output"])
                    elif isinstance(data, dict) and "output" in data:
                        content = str(data["output"])
                    elif isinstance(data, dict):
                        # If it's already a dict but without 'output' key, convert to string
                        import json
                        content = json.dumps(data)
                    else:
                        content = response.text
                except Exception as e:
                    logger.debug(f"Failed to parse n8n response as JSON: {str(e)}")
                    content = response.text

                logger.debug(f"Response from n8n (first 200 chars): {content[:200]}...")

                # Check if content is already valid JSON, if not ensure it's properly wrapped
                tool_calls = None
                try:
                    # Try to parse as JSON to see if it's already valid
                    import json
                    json.loads(content)
                    # Content is valid JSON, use as-is
                    logger.debug("n8n response is valid JSON")
                except json.JSONDecodeError:
                    # Content is plain text, log it for debugging
                    logger.info(f"n8n response is plain text (not JSON), will be handled by parser")
                
                return {
                    "role": "assistant",
                    "content": content,
                    "tool_calls": tool_calls,
                }
        except httpx.ReadTimeout as read_err:
            logger.error(f"Read timeout while waiting for n8n response: {str(read_err)}")
            raise Exception(f"n8n workflow started but did not respond within the timeout period. The workflow may have crashed or is taking too long to process.") from read_err
        except httpx.NetworkError as net_err:
            logger.error(f"Network error calling n8n workflow: {str(net_err)}")
            raise Exception(f"Network error while communicating with n8n workflow. The connection may have been interrupted or the service may be unreachable.") from net_err
        except Exception as e:
            logger.error(f"Unexpected error calling n8n workflow: {str(e)}")
            logger.exception("Full traceback:")
            raise

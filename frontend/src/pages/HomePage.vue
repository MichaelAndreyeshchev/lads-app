<template>
  <!-- Glassmorphic Navbar (outside SimpleBar so it stays fixed) -->
  <ChatNavbar />
  
  <!-- Left Panel Toggle -->
  <div v-if="!isLeftPanelShow" @click="toggleLeftPanel"
    class="panel-toggle-btn">
    <PanelLeft class="size-5 text-[var(--icon-secondary)]" />
  </div>

  <SimpleBar>
    <div
      class="flex flex-col h-full flex-1 min-w-0 mx-auto w-full sm:min-w-[390px] px-5 justify-center items-start gap-2 relative max-w-full sm:max-w-full" 
      style="padding-top: 80px;">
      <div class="w-full max-w-full sm:max-w-[768px] sm:min-w-[390px] mx-auto mt-[180px] mb-auto">
        <div class="w-full flex pl-4 items-center justify-start pb-4">
          <span class="text-[var(--text-primary)] text-start font-serif text-[32px] leading-[40px]" :style="{
            fontFamily:
              'ui-serif, Georgia, Cambria, &quot;Times New Roman&quot;, Times, serif',
          }">
            {{ $t('Hello') }}, {{ currentUser?.fullname }}
            <br />
            <span class="text-[var(--text-tertiary)]">
              {{ $t('What can I do for you?') }}
            </span>
          </span>
        </div>
        <div class="flex flex-col gap-1 w-full">
          <div class="flex flex-col bg-[var(--background-gray-main)] w-full">
            <div class="[&amp;:not(:empty)]:pb-2 bg-[var(--background-gray-main)] rounded-[22px_22px_0px_0px]">
            </div>
            <ChatBox :rows="2" v-model="message" @submit="handleSubmit" :isRunning="false" :attachments="attachments" />
          </div>
        </div>
      </div>
    </div>
  </SimpleBar>
</template>

<script setup lang="ts">
import SimpleBar from '../components/SimpleBar.vue';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import ChatBox from '../components/ChatBox.vue';
import ChatNavbar from '../components/ChatNavbar.vue';
import { createSession } from '../api/agent';
import { showErrorToast } from '../utils/toast';
import { PanelLeft } from 'lucide-vue-next';
import type { FileInfo } from '../api/file';
import { useLeftPanel } from '../composables/useLeftPanel';
import { useFilePanel } from '../composables/useFilePanel';
import { useAuth } from '../composables/useAuth';

const { t } = useI18n();
const router = useRouter();
const message = ref('');
const isSubmitting = ref(false);
const attachments = ref<FileInfo[]>([]);
const { toggleLeftPanel, isLeftPanelShow } = useLeftPanel();
const { hideFilePanel } = useFilePanel();
const { currentUser } = useAuth();

onMounted(() => {
  hideFilePanel();
});

const handleSubmit = async () => {
  if (message.value.trim() && !isSubmitting.value) {
    isSubmitting.value = true;

    try {
      // Create new Agent
      const session = await createSession();
      const sessionId = session.session_id;

      // Navigate to new route with session_id, passing initial message via state
      router.push({
        path: `/chat/${sessionId}`,
        state: {
          message: message.value, files: attachments.value.map((file: FileInfo) => ({
            file_id: file.file_id,
            filename: file.filename,
            content_type: file.content_type,
            size: file.size,
            upload_date: file.upload_date
          }))
        }
      });
    } catch (error) {
      console.error('Failed to create session:', error);
      showErrorToast(t('Failed to create session, please try again later'));
      isSubmitting.value = false;
    }
  }
};
</script>

<style scoped>
/* Panel Toggle Button with glassmorphic design */
.panel-toggle-btn {
  position: fixed;
  left: 16px;
  top: 26px;
  z-index: 999;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  cursor: pointer;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08),
              inset 0 1px 0 rgba(255, 255, 255, 0.3);
  transition: all 0.2s ease;
}

/* Grain texture overlay */
.panel-toggle-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='4.5' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  opacity: 0.15;
  pointer-events: none;
  mix-blend-mode: overlay;
  border-radius: inherit;
}

.panel-toggle-btn:hover {
  background: rgba(255, 255, 255, 0.75);
  transform: translateY(-1px);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.12),
              inset 0 1px 0 rgba(255, 255, 255, 0.4);
}

.panel-toggle-btn:active {
  transform: translateY(0);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08),
              inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

/* Dark Mode */
:global(.dark) .panel-toggle-btn {
  background: rgba(20, 20, 20, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

:global(.dark) .panel-toggle-btn::before {
  opacity: 0.2;
}

:global(.dark) .panel-toggle-btn:hover {
  background: rgba(30, 30, 30, 0.7);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.4),
              inset 0 1px 0 rgba(255, 255, 255, 0.15);
}

@media (max-width: 768px) {
  .panel-toggle-btn {
    left: 12px;
    top: 18px;
    width: 40px;
    height: 40px;
    border-radius: 12px;
  }
}
</style>

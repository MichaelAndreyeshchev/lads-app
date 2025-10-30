<template>
    <div class="pb-3 relative bg-[var(--background-gray-main)]">
        <div class="glass-chatbox">
            <ChatBoxFiles ref="chatBoxFileListRef" :attachments="attachments" />
            <div class="overflow-y-auto pl-4 pr-2">
                <textarea
                    class="flex rounded-md border-input focus-visible:outline-none focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 overflow-hidden flex-1 bg-transparent p-0 pt-[1px] border-0 focus-visible:ring-0 focus-visible:ring-offset-0 w-full placeholder:text-[var(--text-disable)] text-[15px] shadow-none resize-none min-h-[40px]"
                    :rows="rows" :value="modelValue"
                    @input="$emit('update:modelValue', ($event.target as HTMLTextAreaElement).value)"
                    @compositionstart="isComposing = true" @compositionend="isComposing = false"
                    @keydown.enter.exact="handleEnterKeydown" :placeholder="t('Give LADS a task to work on...')"
                    :style="{ height: '46px' }"></textarea>
            </div>
            <footer class="flex flex-row justify-between w-full px-3">
                <div class="flex gap-2 pr-2 items-center">
                    <button @click="uploadFile"
                        class="rounded-full border border-[var(--border-main)] inline-flex items-center justify-center gap-1 clickable cursor-pointer text-xs text-[var(--text-secondary)] hover:bg-[var(--fill-tsp-gray-main)] w-8 h-8 p-0 data-[popover-trigger]:bg-[var(--fill-tsp-gray-main)] shrink-0"
                        aria-expanded="false" aria-haspopup="dialog">
                        <Paperclip :size="16" />
                    </button>
                    <div class="flex gap-1 border border-[var(--border-main)] rounded-full p-1">
                        <button @click="executionMode = 'fast'"
                            :class="executionMode === 'fast' ? 'bg-[var(--Button-primary-black)] text-[var(--text-onblack)]' : 'text-[var(--text-secondary)]'"
                            class="rounded-full px-3 py-1 text-xs font-medium transition-colors hover:bg-[var(--fill-tsp-gray-main)]">
                            Fast
                        </button>
                        <button @click="executionMode = 'deep'"
                            :class="executionMode === 'deep' ? 'bg-[var(--Button-primary-black)] text-[var(--text-onblack)]' : 'text-[var(--text-secondary)]'"
                            class="rounded-full px-3 py-1 text-xs font-medium transition-colors hover:bg-[var(--fill-tsp-gray-main)]">
                            Deep
                        </button>
                    </div>
                </div>
                <div class="flex gap-2">
                    <button v-if="!isRunning || sendEnabled"
                        class="whitespace-nowrap text-sm font-medium focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 text-primary-foreground hover:bg-primary/90 p-0 w-8 h-8 rounded-full flex items-center justify-center transition-colors hover:opacity-90"
                        :class="!sendEnabled ? 'cursor-not-allowed bg-[var(--fill-tsp-white-dark)]' : 'cursor-pointer bg-[var(--Button-primary-black)]'"
                        @click="handleSubmit">
                        <SendIcon :disabled="!sendEnabled" />
                    </button>
                    <button v-else @click="handleStop"
                        class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring bg-[var(--Button-primary-black)] text-[var(--text-onblack)] gap-[4px] hover:opacity-90 rounded-full p-0 w-8 h-8">
                        <div class="w-[10px] h-[10px] bg-[var(--icon-onblack)] rounded-[2px]">
                        </div>
                    </button>
                </div>
            </footer>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue';
import SendIcon from './icons/SendIcon.vue';
import { useI18n } from 'vue-i18n';
import ChatBoxFiles from './ChatBoxFiles.vue';
import { Paperclip } from 'lucide-vue-next';
import type { FileInfo } from '../api/file';

const { t } = useI18n();
const hasTextInput = ref(false);
const isComposing = ref(false);
const chatBoxFileListRef = ref();
const executionMode = ref('deep');

const props = defineProps<{
    modelValue: string;
    rows: number;
    isRunning: boolean;
    attachments: FileInfo[];
}>();

const sendEnabled = computed(() => {
    return chatBoxFileListRef.value?.isAllUploaded && hasTextInput.value;
});

const emit = defineEmits<{
    (e: 'update:modelValue', value: string): void;
    (e: 'submit', executionMode: string): void;
    (e: 'stop'): void;
}>();

const handleEnterKeydown = (event: KeyboardEvent) => {
    if (isComposing.value) {
        // If in input method composition state, do nothing and allow default behavior
        return;
    }

    // Not in input method composition state and has text input, prevent default behavior and submit
    if (sendEnabled.value) {
        event.preventDefault();
        handleSubmit();
    }
};

const handleSubmit = () => {
    if (!sendEnabled.value) return;
    emit('submit', executionMode.value);
};

const handleStop = () => {
    emit('stop');
};

const uploadFile = () => {
    chatBoxFileListRef.value?.uploadFile();
};

watch(() => props.modelValue, (value) => {
    hasTextInput.value = value.trim() !== '';
});
</script>

<style scoped>
.glass-chatbox {
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    border-radius: 24px;
    padding: 0.75rem 0;
    max-height: 300px;
    transition: all 0.2s ease;
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(0, 0, 0, 0.1);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1),
                inset 0 1px 0 0 rgba(255, 255, 255, 0.5);
    overflow: hidden;
}

/* Grain texture overlay */
.glass-chatbox::before {
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
    z-index: 1;
}

.glass-chatbox > * {
    position: relative;
    z-index: 2;
}

:global(.dark) .glass-chatbox {
    background: rgba(20, 20, 20, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.15);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5),
                inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
}

:global(.dark) .glass-chatbox::before {
    opacity: 0.2;
}
</style>

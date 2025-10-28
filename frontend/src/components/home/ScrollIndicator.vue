<template>
  <div class="scroll-indicator" @click="scrollToNext">
    <div class="scroll-text">Scroll to explore</div>
    <div class="scroll-arrow">
      <ChevronDown :size="24" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ChevronDown } from 'lucide-vue-next';

const scrollToNext = () => {
  const videoSection = document.getElementById('video-demo');
  if (videoSection) {
    videoSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
};
</script>

<style scoped>
.scroll-indicator {
  position: relative;
  margin-top: 48px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  animation: bounce 2s ease-in-out infinite;
}

.scroll-indicator:hover {
  transform: translateY(-4px);
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

.scroll-text {
  font-size: 0.875rem;
  font-weight: 500;
  color: rgba(0, 0, 0, 0.6);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  opacity: 0;
  animation: fadeInOut 2s ease-in-out infinite;
  animation-delay: 0.2s;
}

:global(.dark) .scroll-text {
  color: rgba(255, 255, 255, 0.6);
}

@keyframes fadeInOut {
  0%, 100% {
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
}

.scroll-arrow {
  position: relative;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 50%;
  color: #000;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1),
              inset 0 1px 0 0 rgba(255, 255, 255, 0.5);
  overflow: hidden;
  animation: pulse-ring 2s ease-in-out infinite;
}

:global(.dark) .scroll-arrow {
  background: rgba(20, 20, 20, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #fff;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5),
              inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
}

/* Grain texture on arrow */
.scroll-arrow::before {
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

:global(.dark) .scroll-arrow::before {
  opacity: 0.2;
}

/* Pulsing ring effect */
.scroll-arrow::after {
  content: '';
  position: absolute;
  top: -1px;
  left: -1px;
  right: -1px;
  bottom: -1px;
  border: 2px solid rgba(0, 0, 0, 0.2);
  border-radius: 50%;
  animation: ring-pulse 2s ease-in-out infinite;
}

:global(.dark) .scroll-arrow::after {
  border-color: rgba(255, 255, 255, 0.3);
}

@keyframes ring-pulse {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  100% {
    transform: scale(1.8);
    opacity: 0;
  }
}

@keyframes pulse-ring {
  0%, 100% {
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1),
                inset 0 1px 0 0 rgba(255, 255, 255, 0.5);
  }
  50% {
    box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.15),
                inset 0 1px 0 0 rgba(255, 255, 255, 0.6);
  }
}

:global(.dark) .scroll-arrow {
  animation: pulse-ring-dark 2s ease-in-out infinite;
}

@keyframes pulse-ring-dark {
  0%, 100% {
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5),
                inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
  }
  50% {
    box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.7),
                inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
  }
}

.scroll-arrow > svg {
  position: relative;
  z-index: 2;
  animation: arrow-bounce 2s ease-in-out infinite;
}

@keyframes arrow-bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(4px);
  }
}

.scroll-indicator:hover .scroll-arrow {
  transform: scale(1.1);
}

/* Mobile responsive */
@media (max-width: 768px) {
  .scroll-indicator {
    margin-top: 40px;
  }

  .scroll-text {
    font-size: 0.75rem;
  }

  .scroll-arrow {
    width: 40px;
    height: 40px;
  }

  .scroll-arrow > svg {
    width: 20px;
    height: 20px;
  }
}

@media (max-width: 480px) {
  .scroll-indicator {
    margin-top: 32px;
  }

  .scroll-text {
    display: none;
  }

  .scroll-arrow {
    width: 36px;
    height: 36px;
  }

  .scroll-arrow > svg {
    width: 18px;
    height: 18px;
  }
}
</style>


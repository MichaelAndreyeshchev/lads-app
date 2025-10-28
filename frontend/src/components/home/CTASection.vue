<template>
  <div class="glass-container">
    <div class="space-y-6 md:space-y-8">
      <h1 class="text-4xl md:text-6xl lg:text-8xl font-bold tracking-tight leading-[1.1]">
        The DevOps copilot
        <br />
        <span class="text-black/60 dark:text-white/60">that reads your cloud</span>
      </h1>
      <p class="text-base md:text-xl lg:text-2xl text-black/70 dark:text-white/70 max-w-3xl mx-auto font-light leading-relaxed">
        Returns a visual, step-by-step plan to deploy, configure, or fix anything.
      </p>
      
      <div class="button-group">
        <button 
          @click="handleRegister"
          class="cta-btn btn-primary rounded-full transition-all hover:scale-105 hover:shadow-xl">
          <span class="btn-content">
            <Rocket :size="20" />
            <span>get started</span>
          </span>
        </button>
        <button 
          @click="handleLogin"
          class="cta-btn btn-secondary rounded-full transition-all hover:scale-105">
          <span class="btn-content">
            <LogIn :size="20" />
            <span>sign in</span>
          </span>
        </button>
        <button 
          @click="handleBeta"
          class="cta-btn btn-tertiary rounded-full transition-all hover:scale-105">
          <span class="btn-content">
            <Sparkles :size="20" />
            <span>join the beta</span>
          </span>
        </button>
      </div>
      
      <!-- Beta Waitlist Count Tag -->
      <div class="flex justify-center items-center gap-3 mt-6 flex-wrap">
        <div class="beta-tag">
          <span class="beta-dot"></span>
          <span class="beta-text">{{ betaWaitlistCount }} on the beta waitlist</span>
        </div>
        <div class="user-count-tag">
          <span class="user-dot"></span>
          <span class="user-text">{{ usersDeployingCount }} users deploying daily</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import { Rocket, LogIn, Sparkles } from 'lucide-vue-next';

const router = useRouter();

// Manually set counts - update these values as needed
const betaWaitlistCount = ref('0');
const usersDeployingCount = ref('0');

const handleRegister = () => {
  router.push('/login?mode=register');
};

const handleLogin = () => {
  router.push('/login');
};

const handleBeta = () => {
  window.open('https://lads-beta.vercel.app', '_blank');
};
</script>

<style scoped>
.glass-container {
  position: relative;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 32px;
  padding: 3rem 2rem;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1),
              inset 0 1px 0 0 rgba(255, 255, 255, 0.5);
  overflow: hidden;
}

/* Grain texture overlay on glass */
.glass-container::before {
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

.glass-container > * {
  position: relative;
  z-index: 2;
}

:global(.dark) .glass-container {
  background: rgba(20, 20, 20, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5),
              inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
}

:global(.dark) .glass-container::before {
  opacity: 0.2;
}

/* Button Group with responsive sizing */
.button-group {
  display: flex;
  flex-wrap: nowrap;
  gap: 1rem;
  justify-content: center;
  align-items: center;
  margin-top: 2rem;
}

@media (max-width: 768px) {
  .button-group {
    gap: 0.75rem;
  }
}

@media (max-width: 640px) {
  .button-group {
    gap: 0.5rem;
  }
}

@media (max-width: 480px) {
  .button-group {
    gap: 0.375rem;
  }
}

/* Button content with icon */
.btn-content {
  display: flex;
  align-items: center;
  gap: 8px;
  position: relative;
  z-index: 3;
  white-space: nowrap;
}

.btn-content svg {
  flex-shrink: 0;
  min-width: 20px;
  min-height: 20px;
}

@media (max-width: 768px) {
  .btn-content {
    gap: 6px;
  }
  
  .btn-content svg {
    min-width: 18px;
    min-height: 18px;
    width: 18px;
    height: 18px;
  }
}

@media (max-width: 640px) {
  .btn-content {
    gap: 5px;
  }
  
  .btn-content svg {
    min-width: 16px;
    min-height: 16px;
    width: 16px;
    height: 16px;
  }
}

@media (max-width: 480px) {
  .btn-content {
    gap: 4px;
  }
  
  .btn-content svg {
    min-width: 14px;
    min-height: 14px;
    width: 14px;
    height: 14px;
  }
}

/* Base button styles */
.cta-btn {
  padding: 1rem 2rem;
  font-size: 1.125rem;
  font-weight: 500;
}

@media (max-width: 768px) {
  .cta-btn {
    padding: 0.875rem 1.75rem;
    font-size: 1rem;
  }
}

@media (max-width: 640px) {
  .cta-btn {
    padding: 0.75rem 1.5rem;
    font-size: 0.875rem;
  }
}

@media (max-width: 480px) {
  .cta-btn {
    padding: 0.625rem 1.25rem;
    font-size: 0.8125rem;
  }
}

.btn-primary {
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.1);
  cursor: pointer;
  min-width: 160px;
  position: relative;
  overflow: hidden;
  white-space: nowrap;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2),
              inset 0 1px 0 rgba(255, 255, 255, 0.1),
              inset 0 -1px 0 rgba(0, 0, 0, 0.5);
}

@media (max-width: 640px) {
  .btn-primary {
    min-width: 120px;
  }
}

@media (max-width: 480px) {
  .btn-primary {
    min-width: 100px;
  }
}

/* Grain texture overlay */
.btn-primary::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  opacity: 0.5;
  pointer-events: none;
  mix-blend-mode: overlay;
  z-index: 1;
}

/* Glossy highlight */
.btn-primary::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 50%;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.15) 0%, transparent 100%);
  pointer-events: none;
  z-index: 2;
}

.btn-primary:hover {
  background: rgba(0, 0, 0, 0.95);
  transform: translateY(-1px);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.15),
              inset 0 -1px 0 rgba(0, 0, 0, 0.5);
}

.btn-primary:active {
  transform: translateY(0);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.1),
              inset 0 -1px 0 rgba(0, 0, 0, 0.5);
}

:global(.dark) .btn-primary {
  background: rgba(255, 255, 255, 0.85);
  color: #000;
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 4px 16px rgba(255, 255, 255, 0.1),
              inset 0 1px 0 rgba(255, 255, 255, 0.3),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

:global(.dark) .btn-primary::after {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.2) 0%, transparent 100%);
}

:global(.dark) .btn-primary:hover {
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 6px 24px rgba(255, 255, 255, 0.15),
              inset 0 1px 0 rgba(255, 255, 255, 0.4),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  color: #000;
  border: 2px solid rgba(0, 0, 0, 0.2);
  cursor: pointer;
  min-width: 160px;
  position: relative;
  overflow: hidden;
  white-space: nowrap;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08),
              inset 0 1px 0 rgba(255, 255, 255, 0.3),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
}

@media (max-width: 640px) {
  .btn-secondary {
    min-width: 120px;
  }
}

@media (max-width: 480px) {
  .btn-secondary {
    min-width: 100px;
  }
}

/* Grain texture overlay */
.btn-secondary::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  opacity: 0.35;
  pointer-events: none;
  mix-blend-mode: overlay;
  z-index: 1;
}

/* Glossy highlight */
.btn-secondary::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 50%;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.2) 0%, transparent 100%);
  pointer-events: none;
  z-index: 2;
}

:global(.dark) .btn-secondary {
  background: rgba(0, 0, 0, 0.15);
  color: #fff;
  border: 2px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2),
              inset 0 1px 0 rgba(255, 255, 255, 0.15),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

:global(.dark) .btn-secondary::before {
  opacity: 0.4;
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.25);
  border-color: rgba(0, 0, 0, 0.3);
  transform: translateY(-1px);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.12),
              inset 0 1px 0 rgba(255, 255, 255, 0.4),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
}

.btn-secondary:active {
  transform: translateY(0);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08),
              inset 0 1px 0 rgba(255, 255, 255, 0.3),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
}

:global(.dark) .btn-secondary:hover {
  background: rgba(0, 0, 0, 0.25);
  border-color: rgba(255, 255, 255, 0.4);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.2),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

.btn-tertiary {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  color: #000;
  border: 2px solid rgba(0, 0, 0, 0.2);
  cursor: pointer;
  min-width: 160px;
  position: relative;
  overflow: hidden;
  white-space: nowrap;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08),
              inset 0 1px 0 rgba(255, 255, 255, 0.3),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
}

@media (max-width: 640px) {
  .btn-tertiary {
    min-width: 120px;
  }
}

@media (max-width: 480px) {
  .btn-tertiary {
    min-width: 100px;
  }
}

/* Grain texture overlay */
.btn-tertiary::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  opacity: 0.35;
  pointer-events: none;
  mix-blend-mode: overlay;
  z-index: 1;
}

/* Glossy highlight */
.btn-tertiary::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 50%;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.2) 0%, transparent 100%);
  pointer-events: none;
  z-index: 2;
}

:global(.dark) .btn-tertiary {
  background: rgba(0, 0, 0, 0.15);
  color: #fff;
  border: 2px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2),
              inset 0 1px 0 rgba(255, 255, 255, 0.15),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

:global(.dark) .btn-tertiary::before {
  opacity: 0.4;
}

.btn-tertiary:hover {
  background: rgba(255, 255, 255, 0.25);
  border-color: rgba(0, 0, 0, 0.3);
  transform: translateY(-1px);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.12),
              inset 0 1px 0 rgba(255, 255, 255, 0.4),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
}

.btn-tertiary:active {
  transform: translateY(0);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08),
              inset 0 1px 0 rgba(255, 255, 255, 0.3),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
}

:global(.dark) .btn-tertiary:hover {
  background: rgba(0, 0, 0, 0.25);
  border-color: rgba(255, 255, 255, 0.4);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.2),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

/* Beta Waitlist Tag */
.beta-tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: rgba(34, 197, 94, 0.15);
  border: 1px solid rgba(34, 197, 94, 0.3);
  border-radius: 24px;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  box-shadow: 0 2px 12px rgba(34, 197, 94, 0.1),
              inset 0 1px 0 rgba(255, 255, 255, 0.2);
  position: relative;
  overflow: hidden;
}

.beta-tag::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, transparent 50%);
  pointer-events: none;
}

.beta-dot {
  width: 8px;
  height: 8px;
  background: #22c55e;
  border-radius: 50%;
  animation: pulse 2s ease-in-out infinite;
  box-shadow: 0 0 8px rgba(34, 197, 94, 0.6);
  flex-shrink: 0;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
    transform: scale(1);
  }
  50% {
    opacity: 0.7;
    transform: scale(1.1);
  }
}

.beta-text {
  font-size: 14px;
  font-weight: 600;
  color: #22c55e;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  white-space: nowrap;
}

:global(.dark) .beta-tag {
  background: rgba(34, 197, 94, 0.2);
  border: 1px solid rgba(34, 197, 94, 0.4);
  box-shadow: 0 2px 12px rgba(34, 197, 94, 0.15),
              inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

:global(.dark) .beta-text {
  color: #4ade80;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

/* User Count Tag */
.user-count-tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: rgba(59, 130, 246, 0.15);
  border: 1px solid rgba(59, 130, 246, 0.3);
  border-radius: 24px;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  box-shadow: 0 2px 12px rgba(59, 130, 246, 0.1),
              inset 0 1px 0 rgba(255, 255, 255, 0.2);
  position: relative;
  overflow: hidden;
}

.user-count-tag::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, transparent 50%);
  pointer-events: none;
}

.user-dot {
  width: 8px;
  height: 8px;
  background: #3b82f6;
  border-radius: 50%;
  animation: pulse-blue 2s ease-in-out infinite;
  box-shadow: 0 0 8px rgba(59, 130, 246, 0.6);
  flex-shrink: 0;
}

@keyframes pulse-blue {
  0%, 100% {
    opacity: 1;
    transform: scale(1);
  }
  50% {
    opacity: 0.7;
    transform: scale(1.1);
  }
}

.user-text {
  font-size: 14px;
  font-weight: 600;
  color: #3b82f6;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  white-space: nowrap;
}

:global(.dark) .user-count-tag {
  background: rgba(59, 130, 246, 0.2);
  border: 1px solid rgba(59, 130, 246, 0.4);
  box-shadow: 0 2px 12px rgba(59, 130, 246, 0.15),
              inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

:global(.dark) .user-text {
  color: #60a5fa;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

@media (max-width: 768px) {
  .glass-container {
    padding: 2rem 1.5rem;
    border-radius: 24px;
  }
  
  .beta-tag {
    padding: 6px 14px;
    gap: 6px;
  }
  
  .beta-dot {
    width: 6px;
    height: 6px;
  }
  
  .beta-text {
    font-size: 13px;
  }

  .user-count-tag {
    padding: 6px 14px;
    gap: 6px;
  }
  
  .user-dot {
    width: 6px;
    height: 6px;
  }
  
  .user-text {
    font-size: 13px;
  }
}

@media (max-width: 640px) {
  .beta-tag {
    padding: 5px 12px;
    gap: 5px;
  }
  
  .beta-text {
    font-size: 12px;
  }

  .user-count-tag {
    padding: 5px 12px;
    gap: 5px;
  }
  
  .user-text {
    font-size: 12px;
  }
}
</style>


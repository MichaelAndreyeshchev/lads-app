<template>
  <div class="demo-page">
    <Navbar />
    
    <div class="demo-container">
      <div class="glass-container">
        <!-- Hero Section -->
        <div class="demo-hero">
          <h1 class="demo-title">see it in action</h1>
          <p class="demo-subtitle">
            Watch how LADS transforms complex DevOps tasks into simple, automated workflows
          </p>
        </div>

        <!-- Demo Video Section -->
        <div class="demo-video-section">
          <div class="video-card">
            <div class="video-placeholder">
              <div class="play-button">
                <Play :size="48" />
              </div>
              <p class="video-text">watch the demo</p>
            </div>
          </div>
        </div>

        <!-- Feature Highlights -->
        <div class="highlights-section">
          <h2 class="section-title">what you'll see</h2>
          <div class="highlights-list">
            <div class="highlight-item">
              <div class="highlight-icon">
                <MessageSquare :size="20" />
              </div>
              <div class="highlight-content">
                <h3 class="highlight-title">Natural Language Interface</h3>
                <p class="highlight-description">
                  Describe what you want in plain English. No complex commands or syntax required.
                </p>
              </div>
            </div>

            <div class="highlight-item">
              <div class="highlight-icon">
                <Workflow :size="20" />
              </div>
              <div class="highlight-content">
                <h3 class="highlight-title">Visual Step-by-Step Plans</h3>
                <p class="highlight-description">
                  See exactly what will happen before any changes are made. Every step explained clearly.
                </p>
              </div>
            </div>

            <div class="highlight-item">
              <div class="highlight-icon">
                <Zap :size="20" />
              </div>
              <div class="highlight-content">
                <h3 class="highlight-title">Instant Execution</h3>
                <p class="highlight-description">
                  Approve the plan and watch LADS execute it in real-time with full visibility.
                </p>
              </div>
            </div>

            <div class="highlight-item">
              <div class="highlight-icon">
                <Shield :size="20" />
              </div>
              <div class="highlight-content">
                <h3 class="highlight-title">Security Built-In</h3>
                <p class="highlight-description">
                  Every action is logged, validated, and executed within secure sandbox environments.
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- CTA Buttons -->
        <div class="demo-cta">
          <div class="cta-buttons">
            <button class="cta-btn btn-primary" @click="handleStartTrial">
              <span class="btn-content">
                <Rocket :size="20" />
                <span>start free trial</span>
              </span>
            </button>
            <button class="cta-btn btn-secondary" @click="handleScheduleDemo">
              <span class="btn-content">
                <Calendar :size="20" />
                <span>schedule live demo</span>
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import Navbar from '../components/home/Navbar.vue';
import { Play, MessageSquare, Workflow, Zap, Shield, Rocket, Calendar } from 'lucide-vue-next';

const router = useRouter();

const handleStartTrial = () => {
  router.push('/login?mode=register');
};

const handleScheduleDemo = () => {
  window.location.href = 'mailto:demo@lads.ai?subject=Schedule Demo Request';
};
</script>

<style scoped>
.demo-page {
  min-height: 100vh;
  background: #f5f5f5;
  position: relative;
  overflow: hidden;
}

:global(.dark) .demo-page {
  background: #0a0a0a;
}

/* Grainy texture effect */
.demo-page::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='3.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  opacity: 0.4;
  pointer-events: none;
  mix-blend-mode: overlay;
  z-index: 1;
}

:global(.dark) .demo-page::before {
  opacity: 0.25;
}

/* Subtle vignette effect */
.demo-page::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at center, transparent 0%, rgba(0, 0, 0, 0.15) 100%);
  pointer-events: none;
}

:global(.dark) .demo-page::after {
  background: radial-gradient(circle at center, transparent 0%, rgba(0, 0, 0, 0.5) 100%);
}

.demo-container {
  position: relative;
  z-index: 2;
  max-width: 1100px;
  margin: 0 auto;
  padding: 140px 20px 80px;
}

/* Glassmorphic Container */
.glass-container {
  position: relative;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 32px;
  padding: 3rem 2.5rem;
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
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulance type='fractalNoise' baseFrequency='4.5' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
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

/* Hero Section */
.demo-hero {
  text-align: center;
  margin-bottom: 3rem;
}

.demo-title {
  font-size: 4rem;
  font-weight: 700;
  color: #000;
  margin-bottom: 1rem;
  letter-spacing: -1.5px;
  line-height: 1.1;
  text-transform: lowercase;
}

:global(.dark) .demo-title {
  color: #fff;
}

.demo-subtitle {
  font-size: 1.25rem;
  color: rgba(0, 0, 0, 0.7);
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.6;
  font-weight: 300;
}

:global(.dark) .demo-subtitle {
  color: rgba(255, 255, 255, 0.7);
}

/* Video Section */
.demo-video-section {
  margin-bottom: 3rem;
}

.video-card {
  position: relative;
  background: rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 24px;
  padding: 1rem;
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.05);
}

:global(.dark) .video-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.3);
}

.video-placeholder {
  aspect-ratio: 16/9;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2),
              inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

/* Grain texture overlay */
.video-placeholder::before {
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
.video-placeholder::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 50%;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.1) 0%, transparent 100%);
  pointer-events: none;
  z-index: 2;
}

.video-placeholder:hover {
  background: rgba(0, 0, 0, 0.95);
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.15);
}

.video-placeholder:hover .play-button {
  transform: scale(1.1);
  background: rgba(255, 255, 255, 0.3);
}

:global(.dark) .video-placeholder {
  background: rgba(255, 255, 255, 0.85);
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 4px 16px rgba(255, 255, 255, 0.1),
              inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

:global(.dark) .video-placeholder:hover {
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 6px 24px rgba(255, 255, 255, 0.15),
              inset 0 1px 0 rgba(255, 255, 255, 0.4);
}

:global(.dark) .video-placeholder:hover .play-button {
  background: rgba(0, 0, 0, 0.3);
}

.play-button {
  width: 96px;
  height: 96px;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  margin-bottom: 1rem;
  transition: all 0.3s ease;
  position: relative;
  z-index: 3;
  border: 2px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2),
              inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

:global(.dark) .play-button {
  background: rgba(0, 0, 0, 0.2);
  color: #000;
  border: 2px solid rgba(0, 0, 0, 0.2);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1),
              inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.video-text {
  color: rgba(255, 255, 255, 0.9);
  font-size: 1rem;
  font-weight: 500;
  margin: 0;
  position: relative;
  z-index: 3;
  text-transform: lowercase;
  letter-spacing: -0.3px;
}

:global(.dark) .video-text {
  color: rgba(0, 0, 0, 0.9);
}

/* Highlights Section */
.highlights-section {
  margin-bottom: 3rem;
}

.section-title {
  font-size: 2rem;
  font-weight: 600;
  color: #000;
  margin-bottom: 2rem;
  letter-spacing: -0.5px;
  text-align: center;
  text-transform: lowercase;
}

:global(.dark) .section-title {
  color: #fff;
}

.highlights-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.highlight-item {
  display: flex;
  gap: 1.25rem;
  align-items: flex-start;
  padding: 1.5rem;
  background: rgba(0, 0, 0, 0.03);
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 16px;
  transition: all 0.3s ease;
}

.highlight-item:hover {
  background: rgba(0, 0, 0, 0.05);
  border-color: rgba(0, 0, 0, 0.12);
  transform: translateX(4px);
}

:global(.dark) .highlight-item {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

:global(.dark) .highlight-item:hover {
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(255, 255, 255, 0.12);
}

.highlight-icon {
  flex-shrink: 0;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  color: #fff;
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1),
              inset 0 1px 0 rgba(255, 255, 255, 0.1);
  position: relative;
  overflow: hidden;
}

/* Grain texture overlay */
.highlight-icon::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  opacity: 0.4;
  pointer-events: none;
  mix-blend-mode: overlay;
}

:global(.dark) .highlight-icon {
  background: rgba(255, 255, 255, 0.85);
  color: #000;
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 2px 8px rgba(255, 255, 255, 0.05),
              inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.highlight-content {
  flex: 1;
}

.highlight-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #000;
  margin: 0 0 0.5rem 0;
  letter-spacing: -0.3px;
}

:global(.dark) .highlight-title {
  color: #fff;
}

.highlight-description {
  font-size: 0.9375rem;
  color: rgba(0, 0, 0, 0.7);
  line-height: 1.6;
  margin: 0;
}

:global(.dark) .highlight-description {
  color: rgba(255, 255, 255, 0.7);
}

/* CTA Section */
.demo-cta {
  display: flex;
  justify-content: center;
  padding-top: 2rem;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

:global(.dark) .demo-cta {
  border-top-color: rgba(255, 255, 255, 0.1);
}

.cta-buttons {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
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
}

/* Base button styles */
.cta-btn {
  padding: 1rem 2rem;
  font-size: 1.125rem;
  font-weight: 500;
  border-radius: 9999px;
  transition: all 0.2s ease;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  min-width: 180px;
}

.btn-primary {
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2),
              inset 0 1px 0 rgba(255, 255, 255, 0.1),
              inset 0 -1px 0 rgba(0, 0, 0, 0.5);
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
  transform: translateY(-1px) scale(1.05);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.15),
              inset 0 -1px 0 rgba(0, 0, 0, 0.5);
}

.btn-primary:active {
  transform: translateY(0) scale(1);
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
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08),
              inset 0 1px 0 rgba(255, 255, 255, 0.3),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
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
  transform: translateY(-1px) scale(1.05);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.12),
              inset 0 1px 0 rgba(255, 255, 255, 0.4),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
}

.btn-secondary:active {
  transform: translateY(0) scale(1);
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

/* Responsive Styles */
@media (max-width: 768px) {
  .demo-container {
    padding: 100px 16px 60px;
  }

  .glass-container {
    padding: 2rem 1.5rem;
    border-radius: 24px;
  }

  .demo-title {
    font-size: 3rem;
  }

  .demo-subtitle {
    font-size: 1.125rem;
  }

  .section-title {
    font-size: 1.75rem;
  }

  .highlight-item {
    padding: 1.25rem;
  }

  .highlight-icon {
    width: 36px;
    height: 36px;
  }

  .highlight-title {
    font-size: 1rem;
  }

  .highlight-description {
    font-size: 0.875rem;
  }

  .cta-btn {
    padding: 0.875rem 1.75rem;
    font-size: 1rem;
  }

  .btn-content svg {
    width: 18px;
    height: 18px;
  }
}

@media (max-width: 640px) {
  .glass-container {
    padding: 1.75rem 1.25rem;
    border-radius: 20px;
  }

  .demo-title {
    font-size: 2.5rem;
  }

  .demo-subtitle {
    font-size: 1rem;
  }

  .section-title {
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
  }

  .highlight-item {
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
  }

  .highlight-icon {
    width: 32px;
    height: 32px;
  }

  .cta-buttons {
    flex-direction: column;
    width: 100%;
  }

  .cta-btn {
    padding: 0.75rem 1.5rem;
    font-size: 0.875rem;
    width: 100%;
    min-width: auto;
  }

  .btn-content svg {
    width: 16px;
    height: 16px;
  }

  .play-button {
    width: 72px;
    height: 72px;
  }
}

@media (max-width: 480px) {
  .demo-container {
    padding: 90px 12px 40px;
  }

  .glass-container {
    padding: 1.5rem 1rem;
    border-radius: 18px;
  }

  .demo-title {
    font-size: 2rem;
    margin-bottom: 0.75rem;
  }

  .demo-subtitle {
    font-size: 0.9375rem;
  }

  .demo-video-section {
    margin-bottom: 2rem;
  }

  .highlights-section {
    margin-bottom: 2rem;
  }

  .section-title {
    font-size: 1.375rem;
    margin-bottom: 1.25rem;
  }

  .highlights-list {
    gap: 1rem;
  }

  .highlight-item {
    padding: 0.875rem;
  }

  .highlight-title {
    font-size: 0.9375rem;
  }

  .highlight-description {
    font-size: 0.8125rem;
  }

  .demo-cta {
    padding-top: 1.5rem;
  }

  .cta-btn {
    padding: 0.625rem 1.25rem;
    font-size: 0.8125rem;
  }

  .btn-content {
    gap: 6px;
  }

  .btn-content svg {
    width: 14px;
    height: 14px;
  }

  .play-button {
    width: 64px;
    height: 64px;
  }

  .video-text {
    font-size: 0.875rem;
  }
}
</style>

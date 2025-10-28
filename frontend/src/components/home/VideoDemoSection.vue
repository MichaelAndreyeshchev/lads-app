<template>
  <div id="video-demo" class="video-demo-section">
    <div class="max-w-7xl w-full px-4">
      <div class="glass-container">
        <div class="space-y-6 md:space-y-8">
          <div class="section-header">
            <h2 class="section-title">see it in action</h2>
            <p class="section-subtitle">
              Watch how LADS transforms your DevOps workflow with intelligent automation
            </p>
          </div>

          <!-- Video Container -->
          <div class="video-wrapper">
            <div class="video-container">
              <!-- Replace with your actual video source or embed -->
              <video
                v-if="videoSrc"
                :src="videoSrc"
                controls
                playsinline
                class="demo-video"
                poster="/chatting.svg"
              >
                Your browser does not support the video tag.
              </video>
              
              <!-- Placeholder if no video source provided -->
              <div v-else class="video-placeholder">
                <div class="placeholder-content">
                  <div class="play-icon">
                    <Play :size="64" />
                  </div>
                  <p class="placeholder-text">Demo video coming soon</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Feature highlights -->
          <div class="features-grid">
            <div class="feature-card" v-for="(feature, index) in features" :key="index">
              <div class="feature-icon">
                <component :is="feature.icon" :size="20" />
              </div>
              <div class="feature-content">
                <h3 class="feature-title">{{ feature.title }}</h3>
                <p class="feature-description">{{ feature.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { Play, Zap, Eye, GitBranch, Shield } from 'lucide-vue-next';

// Add your video source here
const videoSrc = ref('');

const features = [
  {
    icon: Eye,
    title: 'Visual Plans',
    description: 'Get step-by-step visual guides for every operation'
  },
  {
    icon: GitBranch,
    title: 'Smart Automation',
    description: 'AI-powered workflows that understand your cloud'
  },
  {
    icon: Shield,
    title: 'Enterprise Secure',
    description: 'Built-in security and compliance for production workloads'
  }
];
</script>

<style scoped>
.video-demo-section {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 80px 20px 80px;
  background: #f5f5f5;
  position: relative;
  overflow: hidden;
}

:global(.dark) .video-demo-section {
  background: #0a0a0a;
}

/* Grainy texture effect */
.video-demo-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulance type='fractalNoise' baseFrequency='3.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  opacity: 0.4;
  pointer-events: none;
  mix-blend-mode: overlay;
  z-index: 1;
}

:global(.dark) .video-demo-section::before {
  opacity: 0.25;
}

/* Subtle vignette effect matching CTA section */
.video-demo-section::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at center, transparent 0%, rgba(0, 0, 0, 0.15) 100%);
  pointer-events: none;
  z-index: 1;
}

:global(.dark) .video-demo-section::after {
  background: radial-gradient(circle at center, transparent 0%, rgba(0, 0, 0, 0.5) 100%);
}

.video-demo-section > * {
  position: relative;
  z-index: 2;
}

.section-header {
  text-align: center;
  margin-bottom: 40px;
}

.section-title {
  font-size: 3rem;
  font-weight: 700;
  color: rgba(0, 0, 0, 1);
  margin-bottom: 16px;
  letter-spacing: -0.025em;
  line-height: 1.1;
}

:global(.dark) .section-title {
  color: rgba(255, 255, 255, 1);
}

.section-subtitle {
  font-size: 1.25rem;
  font-weight: 300;
  color: rgba(0, 0, 0, 0.7);
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.6;
}

:global(.dark) .section-subtitle {
  color: rgba(255, 255, 255, 0.7);
}

/* Responsive font sizes to match CTA */
@media (min-width: 768px) {
  .section-title {
    font-size: 4rem;
  }
  
  .section-subtitle {
    font-size: 1.5rem;
  }
}

@media (min-width: 1024px) {
  .section-title {
    font-size: 5rem;
  }
  
  .section-subtitle {
    font-size: 1.75rem;
  }
}

/* Glass Container - matching CTA section */
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

/* Video Wrapper with extra shadow depth */
.video-wrapper {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 900px;
  margin: 0 auto;
  padding: 16px;
  background: rgba(0, 0, 0, 0.03);
  border-radius: 24px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12),
              inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

:global(.dark) .video-wrapper {
  background: rgba(255, 255, 255, 0.03);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.05);
}

.video-container {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  border-radius: 12px;
  overflow: hidden;
  background: #000;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.2),
              inset 0 1px 0 rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(0, 0, 0, 0.1);
}

:global(.dark) .video-container {
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.4),
              inset 0 1px 0 rgba(255, 255, 255, 0.05);
}

.demo-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.video-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.8) 0%, rgba(0, 0, 0, 0.6) 100%);
}

.placeholder-content {
  text-align: center;
  color: #fff;
}

.play-icon {
  margin-bottom: 16px;
  opacity: 0.8;
  animation: pulse-slow 3s ease-in-out infinite;
}

@keyframes pulse-slow {
  0%, 100% {
    opacity: 0.8;
    transform: scale(1);
  }
  50% {
    opacity: 1;
    transform: scale(1.05);
  }
}

.placeholder-text {
  font-size: 1.25rem;
  font-weight: 500;
  opacity: 0.9;
}

/* Features Grid */
.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 32px;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
}

.feature-card {
  position: relative;
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 20px;
  background: rgba(255, 255, 255, 0.4);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 16px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08),
              inset 0 1px 0 rgba(255, 255, 255, 0.3),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
  overflow: hidden;
  cursor: default;
}

/* Grain texture overlay on cards */
.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  opacity: 0.3;
  pointer-events: none;
  mix-blend-mode: overlay;
  z-index: 1;
}

/* Glossy highlight on cards */
.feature-card::after {
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

.feature-card > * {
  position: relative;
  z-index: 3;
}

:global(.dark) .feature-card {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2),
              inset 0 1px 0 rgba(255, 255, 255, 0.1),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

:global(.dark) .feature-card::before {
  opacity: 0.35;
}

.feature-card:hover {
  background: rgba(255, 255, 255, 0.5);
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.12),
              inset 0 1px 0 rgba(255, 255, 255, 0.4),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
}

:global(.dark) .feature-card:hover {
  background: rgba(0, 0, 0, 0.5);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.15),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

.feature-icon {
  flex-shrink: 0;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  color: #fff;
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2),
              inset 0 1px 0 rgba(255, 255, 255, 0.15),
              inset 0 -1px 0 rgba(0, 0, 0, 0.4);
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
}

/* Glossy highlight on icons */
.feature-icon::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 50%;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.2) 0%, transparent 100%);
  pointer-events: none;
}

.feature-card:hover .feature-icon {
  transform: scale(1.05);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.2),
              inset 0 -1px 0 rgba(0, 0, 0, 0.4);
}

:global(.dark) .feature-icon {
  background: rgba(255, 255, 255, 0.85);
  color: #000;
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.1),
              inset 0 1px 0 rgba(255, 255, 255, 0.3),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

:global(.dark) .feature-icon::after {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.25) 0%, transparent 100%);
}

:global(.dark) .feature-card:hover .feature-icon {
  box-shadow: 0 6px 16px rgba(255, 255, 255, 0.15),
              inset 0 1px 0 rgba(255, 255, 255, 0.4),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

.feature-content {
  flex: 1;
  min-width: 0;
}

.feature-title {
  font-size: 1rem;
  font-weight: 600;
  color: #000;
  margin-bottom: 4px;
}

:global(.dark) .feature-title {
  color: #fff;
}

.feature-description {
  font-size: 0.875rem;
  color: rgba(0, 0, 0, 0.65);
  line-height: 1.5;
}

:global(.dark) .feature-description {
  color: rgba(255, 255, 255, 0.65);
}

/* Responsive */
@media (max-width: 1024px) {
  .features-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }
}

@media (max-width: 768px) {
  .video-demo-section {
    padding: 60px 16px 60px;
  }

  .glass-container {
    padding: 2rem 1.5rem;
    border-radius: 24px;
  }

  .section-header {
    margin-bottom: 24px;
  }

  .section-title {
    font-size: 2rem;
  }

  .section-subtitle {
    font-size: 1rem;
  }

  .video-wrapper {
    padding: 12px;
    border-radius: 20px;
  }

  .video-container {
    border-radius: 10px;
  }

  .features-grid {
    margin-top: 24px;
  }

  .feature-card {
    padding: 16px;
  }

  .feature-icon {
    width: 36px;
    height: 36px;
  }
}

@media (max-width: 480px) {
  .video-demo-section {
    padding: 40px 12px 40px;
  }

  .glass-container {
    padding: 1.5rem 1rem;
    border-radius: 20px;
  }

  .section-title {
    font-size: 1.75rem;
  }

  .section-subtitle {
    font-size: 0.9375rem;
  }

  .video-wrapper {
    padding: 10px;
    border-radius: 18px;
  }

  .feature-card {
    padding: 14px;
  }

  .feature-title {
    font-size: 0.9375rem;
  }

  .feature-description {
    font-size: 0.8125rem;
  }
}
</style>


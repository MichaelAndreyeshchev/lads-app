<template>
  <div class="landing-page-wrapper">
    <div class="landing-page hero-section">
      <Navbar />
      <div class="max-w-7xl w-full px-4">
        <div class="text-center">
          <CTASection />
          <ScrollIndicator />
        </div>
      </div>
    </div>
    <VideoDemoSection />
  </div>
</template>

<script setup lang="ts">
import CTASection from './CTASection.vue';
import Navbar from './Navbar.vue';
import VideoDemoSection from './VideoDemoSection.vue';
import ScrollIndicator from './ScrollIndicator.vue';
</script>

<style scoped>
.landing-page-wrapper {
  width: 100%;
  position: relative;
}

.landing-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f5f5f5;
  position: relative;
  overflow: hidden;
}

.hero-section {
  position: relative;
}

:global(.dark) .landing-page {
  background: #0a0a0a;
}

/* Grainy texture effect */
.landing-page::before {
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
}

:global(.dark) .landing-page::before {
  opacity: 0.25;
}

/* Subtle vignette effect */
.landing-page::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at center, transparent 0%, rgba(0, 0, 0, 0.15) 100%);
  pointer-events: none;
}

:global(.dark) .landing-page::after {
  background: radial-gradient(circle at center, transparent 0%, rgba(0, 0, 0, 0.5) 100%);
}
</style>


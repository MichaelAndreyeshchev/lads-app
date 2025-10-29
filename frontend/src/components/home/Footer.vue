<template>
  <footer class="footer-section">
    <div class="footer-container">
      <div class="footer-island">
        <div class="footer-content">
        <!-- Logo and Company Info -->
        <div class="logo-section">
          <div class="logo-group">
            <img src="/lads-logo.png" alt="LADS" class="logo-image" />
            <span class="logo-text">LADS</span>
          </div>
          <p class="company-tagline">The DevOps copilot that reads your cloud</p>
        </div>

        <!-- Links Section -->
        <div class="links-section">
          <div class="footer-column">
            <h4 class="column-title">Product</h4>
            <a href="#" class="footer-link">Features</a>
            <a href="#video-demo" class="footer-link">Demo</a>
            <a href="#" class="footer-link">Pricing</a>
          </div>

          <div class="footer-column">
            <h4 class="column-title">Company</h4>
            <a href="#" class="footer-link">About</a>
            <a href="https://github.com/YourOrg/LADS" target="_blank" class="footer-link">GitHub</a>
            <a href="#" class="footer-link">Contact</a>
          </div>

          <div class="footer-column">
            <h4 class="column-title">Resources</h4>
            <a href="#" class="footer-link">Documentation</a>
            <a href="#" class="footer-link">Blog</a>
            <a href="#" class="footer-link">Support</a>
          </div>
        </div>

        <!-- Copyright -->
        <div class="copyright-section">
          <p class="copyright-text">© {{ currentYear }} LADS. All rights reserved.</p>
        </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const currentYear = computed(() => new Date().getFullYear());
</script>

<style scoped>
.footer-section {
  background: #f5f5f5;
  position: relative;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

:global(.dark) .footer-section {
  background: #0a0a0a;
}

/* Grainy texture effect */
.footer-section::before {
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

:global(.dark) .footer-section::before {
  opacity: 0.25;
}

/* Subtle vignette effect matching CTA section */
.footer-section::after {
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

:global(.dark) .footer-section::after {
  background: radial-gradient(circle at center, transparent 0%, rgba(0, 0, 0, 0.5) 100%);
}

.footer-container {
  position: relative;
  z-index: 2;
  width: 100%;
  display: flex;
  justify-content: center;
  padding: 24px 20px;
  margin-top: 0;
}

.footer-island {
  position: relative;
  width: 100%;
  max-width: 1200px;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 20px;
  padding: 1.5rem 1.25rem;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1),
              inset 0 1px 0 0 rgba(255, 255, 255, 0.5);
  overflow: hidden;
}

/* Grain texture overlay on glass */
.footer-island::before {
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

.footer-island > * {
  position: relative;
  z-index: 2;
}

.footer-content {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

/* Logo Section */
.logo-section {
  display: flex;
  flex-direction: column;
  gap: 4px;
  align-items: flex-start;
}

.logo-group {
  display: flex;
  align-items: center;
  gap: 6px;
}

.logo-image {
  width: 24px;
  height: 24px;
  object-fit: contain;
}

.logo-text {
  font-size: 16px;
  font-weight: 700;
  color: #000;
  letter-spacing: -0.5px;
}

.company-tagline {
  font-size: 11px;
  color: rgba(0, 0, 0, 0.6);
  line-height: 1.4;
  max-width: 300px;
}

/* Links Section */
.links-section {
  display: flex;
  gap: 32px;
  justify-content: flex-start;
}

.footer-column {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.column-title {
  font-size: 10px;
  font-weight: 600;
  color: #000;
  margin: 0 0 3px 0;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.footer-link {
  font-size: 12px;
  color: rgba(0, 0, 0, 0.7);
  text-decoration: none;
  transition: all 0.2s ease;
  position: relative;
  width: fit-content;
}

.footer-link:hover {
  color: #000;
  transform: translateX(2px);
}

/* Copyright Section */
.copyright-section {
  padding-top: 10px;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  text-align: center;
}

.copyright-text {
  font-size: 10px;
  color: rgba(0, 0, 0, 0.5);
  margin: 0;
}

/* Dark Mode */
:global(.dark) .footer-island {
  background: rgba(20, 20, 20, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5),
              inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
}

:global(.dark) .footer-island::before {
  opacity: 0.2;
}

:global(.dark) .logo-text {
  color: #fff;
}

:global(.dark) .company-tagline {
  color: rgba(255, 255, 255, 0.6);
}

:global(.dark) .column-title {
  color: #fff;
}

:global(.dark) .footer-link {
  color: rgba(255, 255, 255, 0.7);
}

:global(.dark) .footer-link:hover {
  color: #fff;
}

:global(.dark) .copyright-section {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

:global(.dark) .copyright-text {
  color: rgba(255, 255, 255, 0.5);
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .footer-container {
    padding: 16px 10px;
  }

  .footer-island {
    padding: 1rem 0.875rem;
    border-radius: 16px;
  }

  .footer-content {
    gap: 10px;
  }

  .logo-section {
    align-items: center;
    text-align: center;
    gap: 3px;
  }

  .logo-group {
    gap: 5px;
  }

  .logo-image {
    width: 20px;
    height: 20px;
  }

  .logo-text {
    font-size: 14px;
  }

  .company-tagline {
    font-size: 10px;
    text-align: center;
  }

  /* Hide most link columns on tablet */
  .links-section {
    gap: 20px;
  }

  .footer-column:nth-child(3) {
    display: none;
  }

  .column-title {
    font-size: 9px;
  }

  .footer-link {
    font-size: 11px;
  }

  .copyright-section {
    padding-top: 8px;
  }

  .copyright-text {
    font-size: 9px;
  }
}

@media (max-width: 480px) {
  .footer-container {
    padding: 12px 10px;
  }

  .footer-island {
    padding: 0.75rem 0.625rem;
    border-radius: 12px;
  }

  .footer-content {
    gap: 8px;
  }

  .logo-section {
    gap: 3px;
    align-items: center;
  }

  .logo-group {
    gap: 5px;
  }

  .logo-image {
    width: 18px;
    height: 18px;
  }

  .logo-text {
    font-size: 13px;
  }

  .company-tagline {
    font-size: 9px;
    text-align: center;
  }

  /* Hide all links on mobile - keep it minimal */
  .links-section {
    display: none;
  }

  .copyright-section {
    padding-top: 6px;
    border-top: none;
    margin-top: 2px;
  }

  .copyright-text {
    font-size: 8px;
  }
}
</style>


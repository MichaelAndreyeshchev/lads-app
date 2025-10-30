<template>
  <div class="about-page">
    <Navbar />
    
    <div class="about-container">
      <div class="glass-container">
        <!-- Hero Section -->
        <div class="about-hero">
          <h1 class="about-title">about <span class="uppercase-text">LADS</span></h1>
          <p class="about-subtitle">
            The DevOps copilot that reads your cloud and returns a visual, step-by-step plan to deploy, configure, or fix anything.
          </p>
        </div>

        <!-- Vision Grid -->
        <div class="vision-grid-section">
          <div class="vision-card">
            <div class="vision-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
                <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
                <line x1="12" y1="22.08" x2="12" y2="12"></line>
              </svg>
            </div>
            <h3 class="vision-title">Visual Control Plane</h3>
            <p class="vision-description">Continuously read live state, generate plans, preflight, and apply with guardrails.</p>
          </div>

          <div class="vision-card">
            <div class="vision-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              </svg>
            </div>
            <h3 class="vision-title">Ship Like a Senior SRE</h3>
            <p class="vision-description">Ask for outcomes in plain English, get verified plans day one.</p>
          </div>

          <div class="vision-card">
            <div class="vision-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
              </svg>
            </div>
            <h3 class="vision-title">Plan-Driven DevOps</h3>
            <p class="vision-description">Move from docs and guesswork to verified, visual plans.</p>
          </div>
        </div>

        <!-- Principles Section -->
        <div class="principles-section">
          <h2 class="section-title">Core Principles</h2>
          <div class="principles-list">
            <div class="principle-item">
              <div class="principle-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="12" r="10"></circle>
                  <polyline points="12 6 12 12 16 14"></polyline>
                </svg>
              </div>
              <div class="principle-content">
                <h3 class="principle-title">Reality > Intent</h3>
                <p class="principle-description">Always read live state first</p>
              </div>
            </div>

            <div class="principle-item">
              <div class="principle-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                  <line x1="3" y1="9" x2="21" y2="9"></line>
                  <line x1="9" y1="21" x2="9" y2="9"></line>
                </svg>
              </div>
              <div class="principle-content">
                <h3 class="principle-title">Visual by Default</h3>
                <p class="principle-description">Interactive flows, not walls of text</p>
              </div>
            </div>

            <div class="principle-item">
              <div class="principle-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                  <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg>
              </div>
              <div class="principle-content">
                <h3 class="principle-title">Guardrails Everywhere</h3>
                <p class="principle-description">Simulate, diff, and roll back every change</p>
              </div>
            </div>

            <div class="principle-item">
              <div class="principle-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <line x1="12" y1="5" x2="12" y2="19"></line>
                  <polyline points="19 12 12 19 5 12"></polyline>
                </svg>
              </div>
              <div class="principle-content">
                <h3 class="principle-title">Short Path to Value</h3>
                <p class="principle-description">One prompt → one plan → one safe apply</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Team Section -->
        <div class="team-section">
          <h2 class="section-title">Meet the Team</h2>
          <div class="team-list">
            <div class="team-member" v-for="member in teamMembers" :key="member.name">
              <div class="member-avatar">
                <img :src="member.avatar" :alt="member.name" />
              </div>
              <div class="member-details">
                <h3 class="member-name">{{ member.name }}</h3>
                <p class="member-role">{{ member.role }}</p>
                <p class="member-description">{{ member.description }}</p>
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
import Navbar from '../components/home/Navbar.vue';

const teamMembers = ref([
  {
    name: 'Michael Andrev',
    role: 'Founder',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Michael',
    description: 'Leading product vision and company strategy. Building the future of DevOps automation.'
  },
  {
    name: 'Anas M',
    role: 'Co-Founder & Systems Engineer',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Anas',
    description: 'Architecting our cloud infrastructure platform and real-time state monitoring system.'
  },
  {
    name: 'Ali Anwar',
    role: 'Co-Founder & ML',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Ali',
    description: 'Building intelligent AI systems and machine learning models for cloud automation.'
  },
  {
    name: 'Andrew Hunter',
    role: 'Marketing & UI/UX',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Andrew',
    description: 'Crafting visual flows and interfaces that make complex infrastructure simple.'
  }
]);
</script>

<style scoped>
.about-page {
  min-height: 100vh;
  background: #f5f5f5;
  position: relative;
  overflow: hidden;
}

:global(.dark) .about-page {
  background: #0a0a0a;
}

/* Grainy texture effect */
.about-page::before {
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

:global(.dark) .about-page::before {
  opacity: 0.25;
}

/* Subtle vignette effect */
.about-page::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at center, transparent 0%, rgba(0, 0, 0, 0.15) 100%);
  pointer-events: none;
}

:global(.dark) .about-page::after {
  background: radial-gradient(circle at center, transparent 0%, rgba(0, 0, 0, 0.5) 100%);
}

.about-container {
  position: relative;
  z-index: 2;
  max-width: 900px;
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
  border-radius: 24px;
  padding: 60px 50px;
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

/* Hero Section */
.about-hero {
  text-align: center;
  margin-bottom: 48px;
  padding-bottom: 48px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

:global(.dark) .about-hero {
  border-bottom-color: rgba(255, 255, 255, 0.1);
}

.about-title {
  font-size: 48px;
  font-weight: 700;
  color: #000;
  margin-bottom: 16px;
  letter-spacing: -1.5px;
  line-height: 1.1;
  text-transform: lowercase;
}

.uppercase-text {
  text-transform: uppercase;
}

:global(.dark) .about-title {
  color: #fff;
}

.about-subtitle {
  font-size: 18px;
  color: rgba(0, 0, 0, 0.7);
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
}

:global(.dark) .about-subtitle {
  color: rgba(255, 255, 255, 0.7);
}

/* Vision Grid Section */
.vision-grid-section {
  margin-bottom: 48px;
  padding-bottom: 48px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
}

:global(.dark) .vision-grid-section {
  border-bottom-color: rgba(255, 255, 255, 0.1);
}

.vision-card {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 24px;
  background: rgba(255, 255, 255, 0.4);
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 16px;
  transition: all 0.3s ease;
}

.vision-card:hover {
  background: rgba(255, 255, 255, 0.6);
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
}

:global(.dark) .vision-card {
  background: rgba(30, 30, 30, 0.4);
  border-color: rgba(255, 255, 255, 0.1);
}

:global(.dark) .vision-card:hover {
  background: rgba(40, 40, 40, 0.6);
}

.vision-icon {
  color: #3b82f6;
  opacity: 1;
}

.vision-card:nth-child(1) .vision-icon {
  color: #3b82f6; /* Blue */
}

.vision-card:nth-child(2) .vision-icon {
  color: #8b5cf6; /* Purple */
}

.vision-card:nth-child(3) .vision-icon {
  color: #ec4899; /* Pink */
}

:global(.dark) .vision-icon {
  opacity: 0.95;
}

:global(.dark) .vision-card:nth-child(1) .vision-icon {
  color: #60a5fa; /* Lighter Blue */
}

:global(.dark) .vision-card:nth-child(2) .vision-icon {
  color: #a78bfa; /* Lighter Purple */
}

:global(.dark) .vision-card:nth-child(3) .vision-icon {
  color: #f472b6; /* Lighter Pink */
}

.vision-title {
  font-size: 18px;
  font-weight: 600;
  color: #000;
  margin: 0;
  letter-spacing: -0.4px;
}

:global(.dark) .vision-title {
  color: #fff;
}

.vision-description {
  font-size: 14px;
  color: rgba(0, 0, 0, 0.7);
  line-height: 1.6;
  margin: 0;
}

:global(.dark) .vision-description {
  color: rgba(255, 255, 255, 0.7);
}

/* Principles Section */
.principles-section {
  margin-bottom: 48px;
  padding-bottom: 48px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

:global(.dark) .principles-section {
  border-bottom-color: rgba(255, 255, 255, 0.1);
}

.section-title {
  font-size: 24px;
  font-weight: 600;
  color: #000;
  margin-bottom: 24px;
  letter-spacing: -0.5px;
}

:global(.dark) .section-title {
  color: #fff;
}

.principles-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.principle-item {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  gap: 16px;
}

.principle-icon {
  flex-shrink: 0;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.05);
  border-radius: 12px;
  color: #000;
}

:global(.dark) .principle-icon {
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
}

.principle-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.principle-title {
  font-size: 16px;
  font-weight: 600;
  color: #000;
  margin: 0;
  letter-spacing: -0.3px;
}

:global(.dark) .principle-title {
  color: #fff;
}

.principle-description {
  font-size: 14px;
  color: rgba(0, 0, 0, 0.6);
  line-height: 1.5;
  margin: 0;
}

:global(.dark) .principle-description {
  color: rgba(255, 255, 255, 0.6);
}

/* Team Section */
.team-section {
  margin-bottom: 0;
}

.team-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.team-member {
  position: relative;
  display: flex;
  align-items: flex-start;
  gap: 20px;
  padding: 24px;
  background: rgba(255, 255, 255, 0.4);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 20px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08),
              inset 0 1px 0 rgba(255, 255, 255, 0.3),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
  overflow: hidden;
  cursor: default;
}

/* Grain texture overlay on member cards */
.team-member::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='4.5' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  opacity: 0.3;
  pointer-events: none;
  mix-blend-mode: overlay;
  z-index: 1;
}

/* Glossy highlight on member cards */
.team-member::after {
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

.team-member > * {
  position: relative;
  z-index: 3;
}

:global(.dark) .team-member {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2),
              inset 0 1px 0 rgba(255, 255, 255, 0.1),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

:global(.dark) .team-member::before {
  opacity: 0.35;
}

.team-member:hover {
  background: rgba(255, 255, 255, 0.5);
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.12),
              inset 0 1px 0 rgba(255, 255, 255, 0.4),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
}

:global(.dark) .team-member:hover {
  background: rgba(0, 0, 0, 0.5);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.15),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

.member-avatar {
  flex-shrink: 0;
  width: 64px;
  height: 64px;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid rgba(0, 0, 0, 0.15);
  background: rgba(255, 255, 255, 0.5);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15),
              inset 0 1px 0 rgba(255, 255, 255, 0.3);
  transition: all 0.3s ease;
}

:global(.dark) .member-avatar {
  border-color: rgba(255, 255, 255, 0.2);
  background: rgba(30, 30, 30, 0.5);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.15);
}

.member-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.team-member:hover .member-avatar {
  transform: scale(1.05);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2),
              inset 0 1px 0 rgba(255, 255, 255, 0.4);
}

:global(.dark) .team-member:hover .member-avatar {
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.4),
              inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.member-details {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.member-name {
  font-size: 1.25rem;
  font-weight: 700;
  color: #000;
  margin: 0;
  letter-spacing: -0.3px;
}

:global(.dark) .member-name {
  color: #fff;
}

.member-role {
  font-size: 1rem;
  font-weight: 600;
  color: rgba(0, 0, 0, 0.75);
  margin: 0;
  letter-spacing: -0.1px;
}

:global(.dark) .member-role {
  color: rgba(255, 255, 255, 0.75);
}

.member-description {
  font-size: 0.9375rem;
  color: rgba(0, 0, 0, 0.65);
  line-height: 1.6;
  margin: 0;
}

:global(.dark) .member-description {
  color: rgba(255, 255, 255, 0.65);
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .about-container {
    padding: 100px 16px 60px;
  }

  .glass-container {
    padding: 40px 28px;
    border-radius: 20px;
  }

  .about-title {
    font-size: 36px;
  }

  .about-subtitle {
    font-size: 16px;
  }

  .section-title {
    font-size: 20px;
  }

  .vision-card {
    padding: 20px;
  }

  .team-member {
    padding: 20px;
    gap: 16px;
    border-radius: 16px;
  }

  .member-avatar {
    width: 56px;
    height: 56px;
  }

  .member-name {
    font-size: 1.125rem;
  }

  .member-role {
    font-size: 0.9375rem;
  }

  .member-description {
    font-size: 0.875rem;
  }
}

@media (max-width: 480px) {
  .about-container {
    padding: 90px 12px 40px;
  }

  .glass-container {
    padding: 32px 20px;
    border-radius: 16px;
  }

  .about-hero {
    margin-bottom: 32px;
    padding-bottom: 32px;
  }

  .about-title {
    font-size: 32px;
  }

  .about-subtitle {
    font-size: 15px;
  }

  .vision-grid-section,
  .principles-section {
    margin-bottom: 32px;
    padding-bottom: 32px;
  }

  .section-title {
    font-size: 18px;
    margin-bottom: 16px;
  }

  .vision-card {
    padding: 18px;
  }

  .vision-title {
    font-size: 16px;
  }

  .vision-description {
    font-size: 13px;
  }

  .principle-icon {
    width: 40px;
    height: 40px;
  }

  .principle-item {
    gap: 12px;
  }

  .principle-title {
    font-size: 15px;
  }

  .principle-description {
    font-size: 13px;
  }

  .team-list {
    gap: 16px;
  }

  .team-member {
    padding: 16px;
    gap: 12px;
  }

  .member-avatar {
    width: 48px;
    height: 48px;
  }

  .member-name {
    font-size: 1rem;
  }

  .member-role {
    font-size: 0.875rem;
  }

  .member-description {
    font-size: 0.8125rem;
  }
}
</style>

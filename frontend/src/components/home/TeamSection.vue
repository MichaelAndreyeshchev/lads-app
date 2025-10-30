<template>
  <div id="team" class="team-section">
    <div class="max-w-7xl w-full px-4">
      <div class="glass-container">
        <div class="space-y-6 md:space-y-8">
          <div class="section-header">
            <h2 class="section-title">meet the team</h2>
            <p class="section-subtitle">
              The talented people behind LADS
            </p>
          </div>

          <!-- Team Members List -->
          <div class="team-list">
            <div 
              v-for="(member, index) in teamMembers" 
              :key="index"
              class="team-member"
            >
              <div class="member-icon">
                <component :is="member.icon" :size="24" />
              </div>
              <div class="member-content">
                <h3 class="member-name">{{ member.name }}</h3>
                <p class="member-role">{{ member.role }}</p>
                <p class="member-description">{{ member.contribution }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { User, Code, Palette, Database, Shield, Zap } from 'lucide-vue-next';

const teamMembers = [
  {
    icon: User,
    name: 'John Smith',
    role: 'Co-Founder & CEO',
    contribution: 'Visionary leader driving product strategy and business development for cloud automation solutions.'
  },
  {
    icon: Code,
    name: 'Sarah Johnson',
    role: 'Lead Engineer',
    contribution: 'Architected the core AI engine and implemented intelligent workflow automation systems.'
  },
  {
    icon: Palette,
    name: 'Mike Chen',
    role: 'Head of Design',
    contribution: 'Created the intuitive glassmorphic interface and designed the visual planning system.'
  },
  {
    icon: Database,
    name: 'Emily Davis',
    role: 'Infrastructure Lead',
    contribution: 'Built scalable cloud infrastructure and optimized deployment pipeline performance.'
  },
  {
    icon: Shield,
    name: 'Alex Turner',
    role: 'Security Engineer',
    contribution: 'Implemented enterprise-grade security features and compliance frameworks.'
  },
  {
    icon: Zap,
    name: 'Lisa Rodriguez',
    role: 'DevOps Specialist',
    contribution: 'Streamlined CI/CD processes and integrated real-time monitoring capabilities.'
  }
];
</script>

<style scoped>
/* CSS Variables for reusable textures */
.team-section {
  --noise-texture: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='4.5' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
}

.team-section {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 80px 20px;
  background: #f5f5f5;
  position: relative;
  overflow: hidden;
  contain: layout style paint;
}

:global(.dark) .team-section {
  background: #0a0a0a;
}

/* Grainy texture effect */
.team-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: var(--noise-texture);
  opacity: 0.4;
  pointer-events: none;
  mix-blend-mode: overlay;
  z-index: 1;
}

:global(.dark) .team-section::before {
  opacity: 0.25;
}

/* Subtle vignette effect */
.team-section::after {
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

:global(.dark) .team-section::after {
  background: radial-gradient(circle at center, transparent 0%, rgba(0, 0, 0, 0.5) 100%);
}

.team-section > * {
  position: relative;
  z-index: 2;
}

.section-header {
  text-align: center;
  margin-bottom: 40px;
  contain: layout style;
}

.section-title {
  font-size: 3rem;
  font-weight: 700;
  color: rgba(0, 0, 0, 1);
  margin-bottom: 16px;
  letter-spacing: -0.025em;
  line-height: 1.1;
  text-rendering: optimizeSpeed;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-display: swap;
  transform: translateZ(0);
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
  text-rendering: optimizeSpeed;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-display: swap;
  transform: translateZ(0);
}

:global(.dark) .section-subtitle {
  color: rgba(255, 255, 255, 0.7);
}

/* Responsive font sizes */
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

/* Glass Container */
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
  will-change: transform;
  transform: translateZ(0);
  contain: layout style paint;
}

/* Grain texture overlay on glass */
.glass-container::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: var(--noise-texture);
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

/* Team List - Vertical Layout */
.team-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 900px;
  margin: 0 auto;
  contain: layout style;
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
  will-change: transform;
  transform: translateZ(0);
  contain: layout style paint;
}

/* Grain texture overlay on member cards */
.team-member::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: var(--noise-texture);
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

/* Member Icon */
.member-icon {
  flex-shrink: 0;
  width: 56px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  color: #fff;
  border-radius: 14px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2),
              inset 0 1px 0 rgba(255, 255, 255, 0.15),
              inset 0 -1px 0 rgba(0, 0, 0, 0.4);
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
}

/* Glossy highlight on icons */
.member-icon::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 50%;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.2) 0%, transparent 100%);
  pointer-events: none;
}

.team-member:hover .member-icon {
  transform: scale(1.05);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.2),
              inset 0 -1px 0 rgba(0, 0, 0, 0.4);
}

:global(.dark) .member-icon {
  background: rgba(255, 255, 255, 0.85);
  color: #000;
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.1),
              inset 0 1px 0 rgba(255, 255, 255, 0.3),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

:global(.dark) .member-icon::after {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.25) 0%, transparent 100%);
}

:global(.dark) .team-member:hover .member-icon {
  box-shadow: 0 6px 16px rgba(255, 255, 255, 0.15),
              inset 0 1px 0 rgba(255, 255, 255, 0.4),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

/* Member Content */
.member-content {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
  contain: layout style;
}

.member-name {
  font-size: 1.25rem;
  font-weight: 700;
  color: #000;
  margin: 0;
  text-rendering: optimizeSpeed;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

:global(.dark) .member-name {
  color: #fff;
}

.member-role {
  font-size: 1rem;
  font-weight: 600;
  color: rgba(0, 0, 0, 0.75);
  margin: 0;
  text-rendering: optimizeSpeed;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

:global(.dark) .member-role {
  color: rgba(255, 255, 255, 0.75);
}

.member-description {
  font-size: 0.9375rem;
  color: rgba(0, 0, 0, 0.65);
  line-height: 1.6;
  margin: 0;
  text-rendering: optimizeSpeed;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

:global(.dark) .member-description {
  color: rgba(255, 255, 255, 0.65);
}

/* Responsive */
@media (max-width: 768px) {
  .team-section {
    padding: 60px 16px;
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

  .team-list {
    gap: 16px;
  }

  .team-member {
    padding: 20px;
    gap: 16px;
    border-radius: 16px;
  }

  .member-icon {
    width: 48px;
    height: 48px;
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
  .team-section {
    padding: 40px 12px;
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

  .team-member {
    padding: 16px;
    gap: 12px;
  }

  .member-icon {
    width: 44px;
    height: 44px;
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


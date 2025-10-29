<template>
  <div class="about-page">
    <Navbar />
    
    <div class="about-container">
      <div class="glass-container">
        <!-- Hero Section -->
        <div class="about-hero">
          <h1 class="about-title">about us</h1>
          <p class="about-subtitle">
            We're building the future of DevOps automation
          </p>
        </div>

        <!-- Mission Section -->
        <div class="mission-section">
          <h2 class="section-title">Our Mission</h2>
          <p class="mission-text">
            At LADS, we believe DevOps should be accessible, intuitive, and powerful. We're creating intelligent AI agents 
            that understand your infrastructure, automate complex workflows, and empower teams to ship faster without sacrificing 
            reliability or security.
          </p>
          <p class="mission-text">
            Founded by engineers who experienced the pain of manual infrastructure management firsthand, we're dedicated to 
            building tools that make DevOps feel less like ops and more like magic.
          </p>
        </div>

        <!-- Team Section -->
        <div class="team-section">
          <h2 class="section-title">Meet the Team</h2>
          <p class="team-intro">
            We're a small but mighty team of engineers, designers, and DevOps enthusiasts building the next generation of cloud automation.
          </p>
          
          <div class="team-grid">
            <div class="team-member" v-for="member in teamMembers" :key="member.name">
              <div class="member-avatar">
                <img :src="member.avatar" :alt="member.name" />
              </div>
              <div class="member-info">
                <h3 class="member-name">{{ member.name }}</h3>
                <p class="member-role">{{ member.role }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Values Section -->
        <div class="values-section">
          <h2 class="section-title">What We Believe</h2>
          <div class="values-list">
            <div class="value-item">
              <h3 class="value-title">Developer First</h3>
              <p class="value-description">
                Tools should work for developers, not the other way around. We prioritize simplicity and developer experience in everything we build.
              </p>
            </div>
            <div class="value-item">
              <h3 class="value-title">Security by Default</h3>
              <p class="value-description">
                Your infrastructure is critical. We build security and compliance into every feature, so you never have to choose between speed and safety.
              </p>
            </div>
            <div class="value-item">
              <h3 class="value-title">Open & Transparent</h3>
              <p class="value-description">
                We believe in building in the open. Our roadmap is public, our community is engaged, and we're always listening to feedback.
              </p>
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
    name: 'Alex Chen',
    role: 'Co-Founder & CEO',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Alex'
  },
  {
    name: 'Sarah Kim',
    role: 'Co-Founder & CTO',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Sarah'
  },
  {
    name: 'Marcus Johnson',
    role: 'Lead Engineer',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Marcus'
  },
  {
    name: 'Priya Patel',
    role: 'Product Designer',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Priya'
  },
  {
    name: 'David Wong',
    role: 'DevOps Architect',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=David'
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

/* Mission Section */
.mission-section {
  margin-bottom: 48px;
  padding-bottom: 48px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

:global(.dark) .mission-section {
  border-bottom-color: rgba(255, 255, 255, 0.1);
}

.section-title {
  font-size: 24px;
  font-weight: 600;
  color: #000;
  margin-bottom: 20px;
  letter-spacing: -0.5px;
}

:global(.dark) .section-title {
  color: #fff;
}

.mission-text {
  font-size: 15px;
  color: rgba(0, 0, 0, 0.7);
  line-height: 1.7;
  margin-bottom: 16px;
}

.mission-text:last-child {
  margin-bottom: 0;
}

:global(.dark) .mission-text {
  color: rgba(255, 255, 255, 0.7);
}

/* Team Section */
.team-section {
  margin-bottom: 48px;
  padding-bottom: 48px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

:global(.dark) .team-section {
  border-bottom-color: rgba(255, 255, 255, 0.1);
}

.team-intro {
  font-size: 15px;
  color: rgba(0, 0, 0, 0.7);
  line-height: 1.7;
  margin-bottom: 32px;
}

:global(.dark) .team-intro {
  color: rgba(255, 255, 255, 0.7);
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 24px;
}

.team-member {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 12px;
}

.member-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid rgba(0, 0, 0, 0.1);
  background: rgba(255, 255, 255, 0.5);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
}

.member-avatar:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
}

:global(.dark) .member-avatar {
  border-color: rgba(255, 255, 255, 0.15);
  background: rgba(30, 30, 30, 0.5);
}

.member-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.member-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.member-name {
  font-size: 14px;
  font-weight: 600;
  color: #000;
  margin: 0;
  line-height: 1.2;
}

:global(.dark) .member-name {
  color: #fff;
}

.member-role {
  font-size: 12px;
  color: rgba(0, 0, 0, 0.6);
  margin: 0;
  line-height: 1.3;
}

:global(.dark) .member-role {
  color: rgba(255, 255, 255, 0.6);
}

/* Values Section */
.values-section {
  margin-bottom: 0;
}

.values-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.value-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.value-title {
  font-size: 16px;
  font-weight: 600;
  color: #000;
  margin: 0;
  letter-spacing: -0.3px;
}

:global(.dark) .value-title {
  color: #fff;
}

.value-description {
  font-size: 14px;
  color: rgba(0, 0, 0, 0.7);
  line-height: 1.7;
  margin: 0;
}

:global(.dark) .value-description {
  color: rgba(255, 255, 255, 0.7);
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

  .mission-text,
  .team-intro {
    font-size: 14px;
  }

  .team-grid {
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 20px;
  }

  .member-avatar {
    width: 64px;
    height: 64px;
  }

  .member-name {
    font-size: 13px;
  }

  .member-role {
    font-size: 11px;
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

  .mission-section,
  .team-section {
    margin-bottom: 32px;
    padding-bottom: 32px;
  }

  .section-title {
    font-size: 18px;
    margin-bottom: 16px;
  }

  .team-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }

  .member-avatar {
    width: 56px;
    height: 56px;
  }

  .values-list {
    gap: 20px;
  }
}
</style>

<template>
  <div class="pricing-page">
    <Navbar />
    
    <div class="pricing-container">
      <!-- Header -->
      <div class="pricing-header">
        <h1 class="pricing-title">Simple pricing</h1>
        <p class="pricing-subtitle">
          Choose the plan that works for you
        </p>
      </div>

      <!-- Pricing Cards -->
      <div class="pricing-grid">
        <!-- Free Tier -->
        <div class="pricing-card">
          <div class="card-header">
            <h3 class="plan-name">Free</h3>
            <div class="plan-price">
              <span class="price">$0</span>
              <span class="period">/month</span>
            </div>
          </div>
          
          <ul class="features-list">
            <li class="feature-item">
              <svg class="check-icon" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
              </svg>
              <span>Basic features</span>
            </li>
            <li class="feature-item">
              <svg class="check-icon" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
              </svg>
              <span>Community support</span>
            </li>
          </ul>
          
          <button class="plan-button plan-button-secondary" @click="handleGetStarted('free')">
            Get started
          </button>
        </div>

        <!-- Pro Tier -->
        <div class="pricing-card pricing-card-featured">
          <div class="featured-badge">Popular</div>
          <div class="card-header">
            <h3 class="plan-name">Pro</h3>
            <div class="plan-price">
              <span class="price">$29</span>
              <span class="period">/month</span>
            </div>
          </div>
          
          <ul class="features-list">
            <li class="feature-item">
              <svg class="check-icon" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
              </svg>
              <span>Everything in Free</span>
            </li>
            <li class="feature-item">
              <svg class="check-icon" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
              </svg>
              <span>Advanced features</span>
            </li>
            <li class="feature-item">
              <svg class="check-icon" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
              </svg>
              <span>Priority support</span>
            </li>
          </ul>
          
          <button class="plan-button plan-button-primary" @click="handleGetStarted('pro')">
            Get started
          </button>
        </div>

        <!-- Enterprise Tier -->
        <div class="pricing-card">
          <div class="card-header">
            <h3 class="plan-name">Enterprise</h3>
            <div class="plan-price">
              <span class="price">Custom</span>
            </div>
          </div>
          
          <ul class="features-list">
            <li class="feature-item">
              <svg class="check-icon" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
              </svg>
              <span>Everything in Pro</span>
            </li>
            <li class="feature-item">
              <svg class="check-icon" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
              </svg>
              <span>Custom solutions</span>
            </li>
            <li class="feature-item">
              <svg class="check-icon" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
              </svg>
              <span>Dedicated support</span>
            </li>
          </ul>
          
          <button class="plan-button plan-button-secondary" @click="handleContactSales">
            Contact sales
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import Navbar from '../components/home/Navbar.vue';

const router = useRouter();

const handleGetStarted = (plan: string) => {
  router.push(`/login?mode=register&plan=${plan}`);
};

const handleContactSales = () => {
  window.location.href = 'mailto:sales@lads.ai';
};
</script>

<style scoped>
.pricing-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
}

:global(.dark) .pricing-page {
  background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
}

.pricing-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 140px 20px 80px;
}

.pricing-header {
  text-align: center;
  margin-bottom: 60px;
}

.pricing-title {
  font-size: 56px;
  font-weight: 700;
  color: #000;
  margin-bottom: 16px;
  letter-spacing: -1.5px;
}

:global(.dark) .pricing-title {
  color: #fff;
}

.pricing-subtitle {
  font-size: 20px;
  color: #666;
  max-width: 600px;
  margin: 0 auto;
}

:global(.dark) .pricing-subtitle {
  color: #aaa;
}

.pricing-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
  max-width: 1200px;
  margin: 0 auto;
}

.pricing-card {
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 24px;
  padding: 40px;
  position: relative;
  transition: all 0.3s ease;
}

.pricing-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
}

:global(.dark) .pricing-card {
  background: rgba(30, 30, 30, 0.8);
  border-color: rgba(255, 255, 255, 0.1);
}

.pricing-card-featured {
  border: 2px solid #000;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
}

:global(.dark) .pricing-card-featured {
  border-color: #fff;
}

.featured-badge {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: #000;
  color: #fff;
  padding: 6px 20px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

:global(.dark) .featured-badge {
  background: #fff;
  color: #000;
}

.card-header {
  text-align: center;
  margin-bottom: 32px;
  padding-bottom: 32px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

:global(.dark) .card-header {
  border-bottom-color: rgba(255, 255, 255, 0.1);
}

.plan-name {
  font-size: 24px;
  font-weight: 700;
  color: #000;
  margin-bottom: 16px;
}

:global(.dark) .plan-name {
  color: #fff;
}

.plan-price {
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 4px;
}

.price {
  font-size: 48px;
  font-weight: 700;
  color: #000;
  letter-spacing: -1px;
}

:global(.dark) .price {
  color: #fff;
}

.period {
  font-size: 18px;
  color: #666;
}

:global(.dark) .period {
  color: #aaa;
}

.features-list {
  list-style: none;
  margin: 0 0 32px 0;
  padding: 0;
}

.feature-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 16px;
  font-size: 15px;
  color: #333;
}

:global(.dark) .feature-item {
  color: #ddd;
}

.check-icon {
  width: 20px;
  height: 20px;
  color: #22c55e;
  flex-shrink: 0;
  margin-top: 2px;
}

.plan-button {
  width: 100%;
  padding: 14px 24px;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.plan-button-primary {
  background: #000;
  color: #fff;
}

.plan-button-primary:hover {
  background: #333;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
}

:global(.dark) .plan-button-primary {
  background: #fff;
  color: #000;
}

:global(.dark) .plan-button-primary:hover {
  background: #f0f0f0;
}

.plan-button-secondary {
  background: rgba(0, 0, 0, 0.05);
  color: #000;
  border: 2px solid rgba(0, 0, 0, 0.1);
}

.plan-button-secondary:hover {
  background: rgba(0, 0, 0, 0.1);
  border-color: rgba(0, 0, 0, 0.2);
  transform: translateY(-2px);
}

:global(.dark) .plan-button-secondary {
  background: rgba(255, 255, 255, 0.05);
  color: #fff;
  border-color: rgba(255, 255, 255, 0.1);
}

:global(.dark) .plan-button-secondary:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.2);
}

@media (max-width: 1024px) {
  .pricing-grid {
    grid-template-columns: 1fr;
    gap: 24px;
    max-width: 500px;
  }
}

@media (max-width: 768px) {
  .pricing-container {
    padding: 100px 16px 60px;
  }

  .pricing-title {
    font-size: 40px;
  }

  .pricing-subtitle {
    font-size: 18px;
  }

  .pricing-card {
    padding: 32px 24px;
  }
}
</style>

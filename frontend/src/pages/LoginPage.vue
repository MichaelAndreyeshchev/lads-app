<template>
  <div class="login-page">
    <Navbar />
    <div class="login-content-wrapper">
      <div class="login-content">
        <div class="w-full max-w-[720px] mb-[32px] max-sm:mb-[24px]">
          <div class="flex flex-col items-center gap-[12px] relative" style="z-index:1">
            <div class="w-[64px] h-[64px] text-[var(--icon-primary)] max-sm:w-[56px] max-sm:h-[56px]">
              <img src="/lads-logo.png" alt="LADS" class="w-full h-full object-contain" />
            </div>
            <h1 class="text-[24px] font-bold text-center text-[var(--text-primary)] max-sm:text-[20px]">
              {{ 
                isResettingPassword ? t('Reset Password') 
                : isRegistering ? t('Register to LADS') 
                : t('Login to LADS') 
              }}
            </h1>
          </div>
        </div>
        <LoginForm v-if="!isRegistering && !isResettingPassword" 
          @success="handleLoginSuccess" 
          @switch-to-register="switchToRegister" 
          @switch-to-reset="switchToReset" />
        <RegisterForm v-else-if="isRegistering && !isResettingPassword" 
          @success="handleLoginSuccess" 
          @switch-to-login="switchToLogin" />
        <ResetPasswordForm v-else-if="isResettingPassword" 
          @back-to-login="switchToLogin" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { Navbar } from '@/components/home'
import LoginForm from '@/components/login/LoginForm.vue'
import RegisterForm from '@/components/login/RegisterForm.vue'
import ResetPasswordForm from '@/components/login/ResetPasswordForm.vue'
import { useAuth } from '@/api'

const { t } = useI18n()

const router = useRouter()
const { isAuthenticated } = useAuth()

// Form state for header display
const isRegistering = ref(false)
const isResettingPassword = ref(false)

// Switch to register mode
const switchToRegister = () => {
  isRegistering.value = true
  isResettingPassword.value = false
}

// Switch to login mode
const switchToLogin = () => {
  isRegistering.value = false
  isResettingPassword.value = false
}

// Switch to reset password mode
const switchToReset = () => {
  isRegistering.value = false
  isResettingPassword.value = true
}

// Handle successful login/registration
const handleLoginSuccess = () => {
    const redirect = router.currentRoute.value.query.redirect as string
    router.push(redirect || '/chat')
}

// Listen for authentication state changes
watch(isAuthenticated, (authenticated) => {
  if (authenticated) {
    handleLoginSuccess()
  }
})

// Check URL query parameter for mode
const checkRouteMode = () => {
  const mode = router.currentRoute.value.query.mode as string
  if (mode === 'register') {
    isRegistering.value = true
  } else if (mode === 'reset') {
    isResettingPassword.value = true
  } else {
    isRegistering.value = false
    isResettingPassword.value = false
  }
}

// Check if already logged in when page loads
onMounted(() => {
  if (isAuthenticated.value) {
    router.push('/chat')
  }
  checkRouteMode()
})

// Watch for route changes
watch(() => router.currentRoute.value.query.mode, () => {
  checkRouteMode()
})
</script>

<style scoped>
.login-page {
  width: 100%;
  min-height: 100vh;
  position: relative;
  background: #f5f5f5;
  overflow: hidden;
}

:global(.dark) .login-page {
  background: #0a0a0a;
}

/* Grainy texture effect */
.login-page::before {
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

:global(.dark) .login-page::before {
  opacity: 0.25;
}

/* Subtle vignette effect */
.login-page::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at center, transparent 0%, rgba(0, 0, 0, 0.15) 100%);
  pointer-events: none;
}

:global(.dark) .login-page::after {
  background: radial-gradient(circle at center, transparent 0%, rgba(0, 0, 0, 0.5) 100%);
}

/* Center the login content */
.login-content-wrapper {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 100px 1rem 60px;
}

.login-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 720px;
}

@media (max-width: 640px) {
  .login-content-wrapper {
    padding: 120px 1rem 60px;
    min-height: calc(100vh - 60px);
  }
}
</style>
<template>
  <div class="w-full max-w-[384px] py-[24px] pt-0 px-[12px] relative" style="z-index:1">
    <div class="glass-form-container">
      <form @submit.prevent="handleSubmit" class="flex flex-col items-stretch gap-[20px]">
        <div class="relative">
          <div class="transition-all duration-500 ease-out opacity-100 scale-100">
            <div class="flex flex-col gap-[12px]">
              <!-- Email field -->
              <div class="flex flex-col items-start">
                <div class="w-full flex items-center justify-between gap-[12px] mb-[8px]">
                  <label for="email"
                    class="text-[13px] text-[var(--text-primary)] font-medium after:content-[&quot;*&quot;] after:text-[var(--function-error)] after:ml-[4px]">
                    <span>{{ t('Email') }}</span>
                  </label>
                </div>
                <input v-model="formData.email"
                  class="rounded-[10px] overflow-hidden text-sm leading-[22px] text-[var(--text-primary)] h-10 disabled:cursor-not-allowed placeholder:text-[var(--text-disable)] bg-[var(--fill-input-chat)] pt-1 pr-1.5 pb-1 pl-3 focus:ring-[1.5px] focus:ring-[var(--border-dark)] w-full"
                  :class="{ 'ring-1 ring-[var(--function-error)]': validationErrors.email }" id="email"
                  placeholder="mail@domain.com" type="email" :disabled="isLoading" @input="validateField('email')"
                  @blur="validateField('email')">
                <div
                  class="text-[13px] text-[var(--function-error)] leading-[18px] overflow-hidden transition-all duration-300 ease-out"
                  :class="validationErrors.email ? 'opacity-100 max-h-[60px] mt-[2px]' : 'opacity-0 max-h-0 mt-0'">
                  {{ validationErrors.email }}
                </div>
              </div>

              <!-- Password field -->
              <div class="flex flex-col items-start">
                <div class="w-full flex items-center justify-between gap-[12px] mb-[8px]">
                  <label for="password"
                    class="text-[13px] text-[var(--text-primary)] font-medium after:content-[&quot;*&quot;] after:text-[var(--function-error)] after:ml-[4px]">
                    <span>{{ t('Password') }}</span>
                  </label>
                  <span
                    class="underline text-[var(--text-tertiary)] text-[13px] leading-[18px] transition-opacity cursor-pointer select-none hover:opacity-80 active:opacity-80"
                    @click="emits('switchToReset')">{{ t('Forgot Password?') }}</span>
                </div>
                <div class="relative w-full">
                  <input v-model="formData.password"
                    class="rounded-[10px] overflow-hidden text-sm leading-[22px] text-[var(--text-primary)] h-10 w-full disabled:cursor-not-allowed placeholder:text-[var(--text-disable)] bg-[var(--fill-input-chat)] pt-1 pb-1 pl-3 focus:ring-[1.5px] focus:ring-[var(--border-dark)] pr-[40px]"
                    :class="{ 'ring-1 ring-[var(--function-error)]': validationErrors.password }"
                    :placeholder="t('Enter password')" :type="showPassword ? 'text' : 'password'"
                    :disabled="isLoading" @input="validateField('password')" @blur="validateField('password')">
                  <div
                    class="text-[var(--icon-tertiary)] absolute z-30 right-[6px] top-[50%] p-[6px] rounded-md transform -translate-y-1/2 cursor-pointer hover:text-[--icon-primary] active:opacity-90 transition-all"
                    @click="showPassword = !showPassword">
                    <Eye v-if="showPassword" :size="16" />
                    <EyeOff v-else :size="16" />
                  </div>
                </div>
                <div
                  class="text-[13px] text-[var(--function-error)] leading-[18px] overflow-hidden transition-all duration-300 ease-out"
                  :class="validationErrors.password ? 'opacity-100 max-h-[60px] mt-[2px]' : 'opacity-0 max-h-0 mt-0'">
                  {{ validationErrors.password }}
                </div>
              </div>

              <!-- Submit button -->
              <button type="submit"
                class="inline-flex items-center justify-center whitespace-nowrap font-medium transition-colors h-[40px] px-[16px] rounded-[10px] gap-[6px] text-sm min-w-16 w-full"
                :class="isFormValid && !isLoading
                  ? 'bg-[var(--Button-primary-black)] text-[var(--text-onblack)] hover:opacity-90 active:opacity-80'
                  : 'bg-[#898988] dark:bg-[#939393] text-[var(--text-onblack)] opacity-50 cursor-not-allowed'"
                :disabled="!isFormValid || isLoading">
                <LoaderCircle v-if="isLoading" :size="16" class="animate-spin" />
                <span>{{ isLoading ? t('Processing...') : t('Login') }}</span>
              </button>
            </div>
          </div>
        </div>

        <!-- Toggle to register -->
        <div v-if="hasRegister" class="text-center text-[13px] leading-[18px] text-[var(--text-tertiary)] mt-[8px]">
          <span>{{ t('Don\'t have an account?') }}</span>
          <span
            class="ms-[8px] text-[var(--text-secondary)] cursor-pointer select-none hover:opacity-80 active:opacity-70 transition-all underline"
            @click="emits('switchToRegister')">
            {{ t('Register') }}
          </span>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { Eye, EyeOff, LoaderCircle } from 'lucide-vue-next'
import { useAuth } from '@/api'
import { validateUserInput } from '@/utils/auth'
import { showErrorToast, showSuccessToast } from '@/utils/toast'
import { getCachedAuthProvider } from '@/api/auth'

const { t } = useI18n()

// Emits
const emits = defineEmits<{
  success: []
  switchToRegister: []
  switchToReset: []
}>()

const { login, isLoading, authError } = useAuth()
const hasRegister = ref(true)

// Form state
const showPassword = ref(false)

// Form data
const formData = ref({
  email: '',
  password: ''
})

// Validation errors
const validationErrors = ref<Record<string, string>>({})

// Clear form
const clearForm = () => {
  formData.value = {
    email: '',
    password: ''
  }
  validationErrors.value = {}
}

// Validate single field
const validateField = (field: string) => {
  const errors: Record<string, string> = {}

  if (field === 'email') {
    const result = validateUserInput({ email: formData.value.email })
    if (result.errors.email) {
      errors.email = result.errors.email
    }
  }

  if (field === 'password') {
    const result = validateUserInput({ password: formData.value.password })
    if (result.errors.password) {
      errors.password = result.errors.password
    }
  }

  // Update error state
  Object.keys(errors).forEach(key => {
    validationErrors.value[key] = errors[key]
  })

  // Clear fixed errors
  if (!errors[field]) {
    delete validationErrors.value[field]
  }
}

// Validate entire form
const validateForm = () => {
  const data = {
    email: formData.value.email,
    password: formData.value.password
  }

  const result = validateUserInput(data)
  validationErrors.value = { ...result.errors }

  return Object.keys(validationErrors.value).length === 0
}

// Check if form is valid
const isFormValid = computed(() => {
  const hasRequiredFields = formData.value.email.trim() && formData.value.password.trim()
  const hasNoErrors = Object.keys(validationErrors.value).length === 0
  return hasRequiredFields && hasNoErrors
})

// Submit form
const handleSubmit = async () => {
  if (!validateForm()) {
    return
  }

  try {
    await login({
      email: formData.value.email,
      password: formData.value.password
    })
    
    // Login success message
    showSuccessToast(t('Login successful! Welcome back'))
    
    // Emit success event
    emits('success')
  } catch (error: any) {
    console.error('Login failed:', error)
    // Display error message using toast
    showErrorToast(authError.value || t('Login failed, please try again'))
  }
}

onMounted(async () => {
  const authProvider = await getCachedAuthProvider()
  // Default to showing register; hide only if provider explicitly disallows it
  hasRegister.value = authProvider === null ? true : authProvider === 'password'
})

// Expose clearForm method for parent component
defineExpose({
  clearForm
})
</script>

<style scoped>
.glass-form-container {
  position: relative;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 20px;
  padding: 2rem 1.5rem;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1),
              inset 0 1px 0 0 rgba(255, 255, 255, 0.5);
  overflow: hidden;
}

/* Grain texture overlay on glass */
.glass-form-container::before {
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

.glass-form-container > * {
  position: relative;
  z-index: 2;
}

:global(.dark) .glass-form-container {
  background: rgba(20, 20, 20, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5),
              inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
}

:global(.dark) .glass-form-container::before {
  opacity: 0.2;
}
</style>
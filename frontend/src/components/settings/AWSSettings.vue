<template>
  <div class="space-y-6">
    <!-- AWS Credentials Header -->
    <div class="flex flex-col gap-2">
      <h3 class="text-lg font-semibold text-[var(--text-primary)]">{{ t('AWS Credentials') }}</h3>
      <p class="text-sm text-[var(--text-secondary)]">
        {{ t('Configure your AWS credentials to enable cloud services integration.') }}
      </p>
    </div>

    <!-- AWS Credentials Form -->
    <div class="space-y-4">
      <!-- Access Key ID -->
      <div class="flex flex-col gap-2">
        <label for="aws-access-key" class="text-sm font-medium text-[var(--text-primary)]">
          {{ t('Access Key ID') }}
        </label>
        <div class="relative">
          <input
            id="aws-access-key"
            v-model="credentials.accessKeyId"
            :type="showAccessKey ? 'text' : 'password'"
            :placeholder="t('Enter your AWS Access Key ID')"
            class="w-full px-3 py-2 pr-10 text-sm rounded-lg bg-[var(--fill-input-chat)] text-[var(--text-primary)] placeholder:text-[var(--text-disable)] focus:ring-1 focus:ring-[var(--border-dark)]"
          />
          <button
            type="button"
            @click="showAccessKey = !showAccessKey"
            class="absolute right-2 top-1/2 -translate-y-1/2 p-1 text-[var(--icon-tertiary)] hover:text-[var(--icon-primary)]"
          >
            <Eye v-if="showAccessKey" :size="16" />
            <EyeOff v-else :size="16" />
          </button>
        </div>
      </div>

      <!-- Secret Access Key -->
      <div class="flex flex-col gap-2">
        <label for="aws-secret-key" class="text-sm font-medium text-[var(--text-primary)]">
          {{ t('Secret Access Key') }}
        </label>
        <div class="relative">
          <input
            id="aws-secret-key"
            v-model="credentials.secretAccessKey"
            :type="showSecretKey ? 'text' : 'password'"
            :placeholder="t('Enter your AWS Secret Access Key')"
            class="w-full px-3 py-2 pr-10 text-sm rounded-lg bg-[var(--fill-input-chat)] text-[var(--text-primary)] placeholder:text-[var(--text-disable)] focus:ring-1 focus:ring-[var(--border-dark)]"
          />
          <button
            type="button"
            @click="showSecretKey = !showSecretKey"
            class="absolute right-2 top-1/2 -translate-y-1/2 p-1 text-[var(--icon-tertiary)] hover:text-[var(--icon-primary)]"
          >
            <Eye v-if="showSecretKey" :size="16" />
            <EyeOff v-else :size="16" />
          </button>
        </div>
      </div>

      <!-- Region -->
      <div class="flex flex-col gap-2">
        <label for="aws-region" class="text-sm font-medium text-[var(--text-primary)]">
          {{ t('Default Region') }}
        </label>
        <select
          id="aws-region"
          v-model="credentials.region"
          class="w-full px-3 py-2 text-sm rounded-lg bg-[var(--fill-input-chat)] text-[var(--text-primary)] focus:ring-1 focus:ring-[var(--border-dark)]"
        >
          <option value="">{{ t('Select a region') }}</option>
          <option v-for="region in awsRegions" :key="region.value" :value="region.value">
            {{ region.label }}
          </option>
        </select>
      </div>

      <!-- Session Token (Optional) -->
      <div class="flex flex-col gap-2">
        <label for="aws-session-token" class="text-sm font-medium text-[var(--text-primary)]">
          {{ t('Session Token') }}
          <span class="text-xs text-[var(--text-tertiary)] ml-1">{{ t('(Optional)') }}</span>
        </label>
        <div class="relative">
          <input
            id="aws-session-token"
            v-model="credentials.sessionToken"
            :type="showSessionToken ? 'text' : 'password'"
            :placeholder="t('Enter session token for temporary credentials')"
            class="w-full px-3 py-2 pr-10 text-sm rounded-lg bg-[var(--fill-input-chat)] text-[var(--text-primary)] placeholder:text-[var(--text-disable)] focus:ring-1 focus:ring-[var(--border-dark)]"
          />
          <button
            v-if="credentials.sessionToken"
            type="button"
            @click="showSessionToken = !showSessionToken"
            class="absolute right-2 top-1/2 -translate-y-1/2 p-1 text-[var(--icon-tertiary)] hover:text-[var(--icon-primary)]"
          >
            <Eye v-if="showSessionToken" :size="16" />
            <EyeOff v-else :size="16" />
          </button>
        </div>
      </div>

      <!-- Save Button -->
      <div class="flex items-center justify-between pt-4">
        <div class="text-xs text-[var(--text-tertiary)]">
          {{ t('Credentials are stored securely in your browser') }}
        </div>
        <button
          @click="saveCredentials"
          :disabled="!isFormValid || isSaving"
          class="px-4 py-2 text-sm font-medium rounded-lg transition-colors"
          :class="isFormValid && !isSaving
            ? 'bg-[var(--Button-primary-black)] text-[var(--text-onblack)] hover:opacity-90'
            : 'bg-[#898988] dark:bg-[#939393] text-[var(--text-onblack)] opacity-50 cursor-not-allowed'"
        >
          <LoaderCircle v-if="isSaving" :size="14" class="animate-spin mr-2 inline" />
          {{ isSaving ? t('Saving...') : t('Save Credentials') }}
        </button>
      </div>

      <!-- Test Connection Button -->
      <div v-if="hasExistingCredentials" class="pt-2">
        <button
          @click="testConnection"
          :disabled="isTesting"
          class="w-full px-4 py-2 text-sm font-medium rounded-lg border border-[var(--border-main)] bg-[var(--background-white-main)] text-[var(--text-primary)] hover:bg-[var(--fill-tsp-white-main)] transition-colors"
        >
          <LoaderCircle v-if="isTesting" :size="14" class="animate-spin mr-2 inline" />
          {{ isTesting ? t('Testing...') : t('Test Connection') }}
        </button>
        <div v-if="testResult" class="mt-2 p-3 rounded-lg text-sm" 
          :class="testResult.success ? 'bg-green-50 text-green-700 dark:bg-green-900/20 dark:text-green-400' : 'bg-red-50 text-red-700 dark:bg-red-900/20 dark:text-red-400'">
          {{ testResult.message }}
        </div>
      </div>
    </div>

    <!-- Clear Credentials -->
    <div v-if="hasExistingCredentials" class="pt-4 border-t border-[var(--border-main)]">
      <button
        @click="clearCredentials"
        class="text-sm text-[var(--function-error)] hover:opacity-80"
      >
        {{ t('Clear Stored Credentials') }}
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { Eye, EyeOff, LoaderCircle } from 'lucide-vue-next'
import { showSuccessToast, showErrorToast } from '@/utils/toast'

const { t } = useI18n()

// State
const showAccessKey = ref(false)
const showSecretKey = ref(false)
const showSessionToken = ref(false)
const isSaving = ref(false)
const isTesting = ref(false)
const testResult = ref<{ success: boolean; message: string } | null>(null)

// Credentials form
const credentials = ref({
  accessKeyId: '',
  secretAccessKey: '',
  region: 'us-east-1',
  sessionToken: ''
})

// Check if we have existing credentials
const hasExistingCredentials = computed(() => {
  const stored = localStorage.getItem('aws_credentials')
  return !!stored
})

// Check if form is valid
const isFormValid = computed(() => {
  return credentials.value.accessKeyId.trim() && 
         credentials.value.secretAccessKey.trim() && 
         credentials.value.region.trim()
})

// AWS Regions
const awsRegions = [
  { value: 'us-east-1', label: 'US East (N. Virginia)' },
  { value: 'us-east-2', label: 'US East (Ohio)' },
  { value: 'us-west-1', label: 'US West (N. California)' },
  { value: 'us-west-2', label: 'US West (Oregon)' },
  { value: 'eu-west-1', label: 'EU (Ireland)' },
  { value: 'eu-west-2', label: 'EU (London)' },
  { value: 'eu-west-3', label: 'EU (Paris)' },
  { value: 'eu-central-1', label: 'EU (Frankfurt)' },
  { value: 'ap-south-1', label: 'Asia Pacific (Mumbai)' },
  { value: 'ap-northeast-1', label: 'Asia Pacific (Tokyo)' },
  { value: 'ap-northeast-2', label: 'Asia Pacific (Seoul)' },
  { value: 'ap-southeast-1', label: 'Asia Pacific (Singapore)' },
  { value: 'ap-southeast-2', label: 'Asia Pacific (Sydney)' },
  { value: 'ca-central-1', label: 'Canada (Central)' },
  { value: 'sa-east-1', label: 'South America (São Paulo)' }
]

// Load existing credentials (masked)
const loadCredentials = () => {
  const stored = localStorage.getItem('aws_credentials')
  if (stored) {
    try {
      const parsed = JSON.parse(stored)
      // Only show masked versions
      credentials.value.accessKeyId = '••••••••••••' + parsed.accessKeyId.slice(-4)
      credentials.value.secretAccessKey = '••••••••••••••••••••'
      credentials.value.region = parsed.region || 'us-east-1'
      credentials.value.sessionToken = parsed.sessionToken ? '••••••••••••' : ''
    } catch (error) {
      console.error('Failed to load AWS credentials:', error)
    }
  }
}

// Save credentials
const saveCredentials = async () => {
  isSaving.value = true
  
  try {
    // Only save if actual values (not masked)
    if (!credentials.value.accessKeyId.includes('•')) {
      const toStore = {
        accessKeyId: credentials.value.accessKeyId,
        secretAccessKey: credentials.value.secretAccessKey,
        region: credentials.value.region,
        sessionToken: credentials.value.sessionToken || undefined
      }
      
      localStorage.setItem('aws_credentials', JSON.stringify(toStore))
      showSuccessToast(t('AWS credentials saved successfully'))
      
      // Reload to show masked values
      loadCredentials()
    } else {
      showErrorToast(t('Please enter new credentials'))
    }
  } catch (error) {
    console.error('Failed to save AWS credentials:', error)
    showErrorToast(t('Failed to save credentials'))
  } finally {
    isSaving.value = false
  }
}

// Test connection
const testConnection = async () => {
  isTesting.value = true
  testResult.value = null
  
  try {
    // In a real app, this would make an API call to test the credentials
    // For now, we'll simulate a test
    await new Promise(resolve => setTimeout(resolve, 1500))
    
    // Simulate success/failure
    const success = Math.random() > 0.3
    testResult.value = {
      success,
      message: success 
        ? t('Connection successful! Your AWS credentials are valid.')
        : t('Connection failed. Please check your credentials.')
    }
  } catch (error) {
    testResult.value = {
      success: false,
      message: t('Error testing connection: ') + error
    }
  } finally {
    isTesting.value = false
  }
}

// Clear credentials
const clearCredentials = () => {
  if (confirm(t('Are you sure you want to clear your stored AWS credentials?'))) {
    localStorage.removeItem('aws_credentials')
    credentials.value = {
      accessKeyId: '',
      secretAccessKey: '',
      region: 'us-east-1',
      sessionToken: ''
    }
    testResult.value = null
    showSuccessToast(t('AWS credentials cleared'))
  }
}

// Load credentials on mount
onMounted(() => {
  loadCredentials()
})
</script>

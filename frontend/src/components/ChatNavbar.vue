<template>
  <nav class="navbar-container" :class="{ 'with-panel': isLeftPanelShow }">
    <div class="navbar-island">
      <div class="navbar-content">
        <!-- Logo -->
        <div class="logo-section" @click="handleLogoClick">
          <img src="/lads-logo.png" alt="LADS" class="logo-image" />
          <span class="logo-text">LADS</span>
        </div>

        <!-- Chat Title (center) - only show if title is provided -->
        <div v-if="title" class="chat-title-section">
          <span class="chat-title">{{ title }}</span>
        </div>

        <!-- Right Actions -->
        <div class="nav-actions" :class="{ 'ml-auto': !title }">
          <button @click="handleFileListShow" class="icon-btn" title="Search files">
            <FileSearch :size="18" />
          </button>
          <div v-if="currentUser" @click="toggleUserMenu" ref="userMenuTrigger"
            class="user-avatar">
            {{ avatarLetter }}
          </div>
        </div>
      </div>
    </div>
  </nav>
  
  <!-- User Menu Dropdown (outside navbar for proper z-index) -->
  <div v-if="isUserMenuOpen" ref="userMenuRef"
    class="fixed z-[1001]"
    :style="{
      top: userMenuPosition.y + 'px',
      left: userMenuPosition.x + 'px',
    }">
    <UserMenu @close="isUserMenuOpen = false" />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, nextTick, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import { FileSearch } from 'lucide-vue-next';
import { useAuth } from '../composables/useAuth';
import { useLeftPanel } from '../composables/useLeftPanel';
import UserMenu from './UserMenu.vue';

interface Props {
  title?: string;
}

const props = withDefaults(defineProps<Props>(), {
  title: 'Chat'
});

const emit = defineEmits<{
  (e: 'fileListShow'): void;
}>();

const router = useRouter();
const { currentUser } = useAuth();
const { isLeftPanelShow } = useLeftPanel();

// User menu state
const isUserMenuOpen = ref(false);
const userMenuTrigger = ref<HTMLElement>();
const userMenuRef = ref<HTMLElement>();
const userMenuPosition = ref({ x: 0, y: 0 });

// Get first letter of user's fullname for avatar display
const avatarLetter = computed(() => {
  return currentUser.value?.fullname?.charAt(0)?.toUpperCase() || 'U';
});

const handleLogoClick = () => {
  router.push('/');
};

const handleFileListShow = () => {
  emit('fileListShow');
};

// Toggle user menu
const toggleUserMenu = async (event: MouseEvent) => {
  event.stopPropagation();
  
  if (isUserMenuOpen.value) {
    isUserMenuOpen.value = false;
    return;
  }
  
  // Calculate position
  if (userMenuTrigger.value) {
    const rect = userMenuTrigger.value.getBoundingClientRect();
    
    // Wait for menu to render to get its dimensions
    isUserMenuOpen.value = true;
    await nextTick();
    
    const menuWidth = userMenuRef.value?.offsetWidth || 300;
    const menuHeight = userMenuRef.value?.offsetHeight || 200;
    const padding = 16;
    
    // Calculate viewport dimensions
    const viewportWidth = window.innerWidth;
    const viewportHeight = window.innerHeight;
    
    // Try to center below the avatar
    let x = rect.left + rect.width / 2 - menuWidth / 2;
    let y = rect.bottom + 8;
    
    // Adjust horizontal position if menu overflows viewport
    if (x + menuWidth > viewportWidth - padding) {
      x = viewportWidth - menuWidth - padding;
    }
    if (x < padding) {
      x = padding;
    }
    
    // Adjust vertical position if menu overflows bottom of viewport
    if (y + menuHeight > viewportHeight - padding) {
      y = rect.top - menuHeight - 8;
    }
    
    userMenuPosition.value = { x, y };
  } else {
    isUserMenuOpen.value = true;
  }
};

// Handle click outside to close user menu
const handleUserMenuClickOutside = (event: MouseEvent) => {
  if (isUserMenuOpen.value && 
      userMenuRef.value && 
      !userMenuRef.value.contains(event.target as Node) &&
      userMenuTrigger.value &&
      !userMenuTrigger.value.contains(event.target as Node)) {
    isUserMenuOpen.value = false;
  }
};

onMounted(() => {
  document.addEventListener('click', handleUserMenuClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', handleUserMenuClickOutside);
});
</script>

<style scoped>
.navbar-container {
  position: fixed;
  top: 20px;
  left: 80px; /* Start after the side panel button (16px + 44px + 20px gap) */
  right: 20px;
  z-index: 1000;
  pointer-events: none;
  transition: left 0.28s cubic-bezier(0.4, 0, 0.2, 1);
}

.navbar-container.with-panel {
  left: 320px; /* Left panel width (300px) + 20px gap */
}

.navbar-island {
  position: relative;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 20px;
  padding: 12px 24px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08),
              inset 0 1px 0 rgba(255, 255, 255, 0.5);
  overflow: hidden;
  transition: all 0.3s ease;
  pointer-events: auto;
}

.navbar-island:hover {
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12),
              inset 0 1px 0 rgba(255, 255, 255, 0.6);
}

/* Grain texture overlay */
.navbar-island::before {
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

.navbar-content {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

/* Logo Section */
.logo-section {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  user-select: none;
  flex-shrink: 0;
}

.logo-image {
  width: 32px;
  height: 32px;
  object-fit: contain;
}

.logo-text {
  font-size: 20px;
  font-weight: 700;
  color: #000;
  letter-spacing: -0.5px;
}

/* Chat Title Section */
.chat-title-section {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 0;
}

.chat-title {
  color: #000;
  font-size: 16px;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%;
}

/* Action Buttons */
.nav-actions {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}

.nav-actions.ml-auto {
  margin-left: auto;
}

.icon-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  color: #000;
  border: 2px solid rgba(0, 0, 0, 0.2);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08),
              inset 0 1px 0 rgba(255, 255, 255, 0.3),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

/* Grain texture overlay on icon button */
.icon-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  opacity: 0.35;
  pointer-events: none;
  mix-blend-mode: overlay;
  z-index: 1;
}

/* Glossy highlight on icon button */
.icon-btn::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 50%;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.2) 0%, transparent 100%);
  pointer-events: none;
  z-index: 2;
}

.icon-btn > * {
  position: relative;
  z-index: 3;
}

.icon-btn:hover {
  background: rgba(255, 255, 255, 0.25);
  border-color: rgba(0, 0, 0, 0.3);
  transform: translateY(-1px);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.12),
              inset 0 1px 0 rgba(255, 255, 255, 0.4),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
}

.icon-btn:active {
  transform: translateY(0);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08),
              inset 0 1px 0 rgba(255, 255, 255, 0.3),
              inset 0 -1px 0 rgba(0, 0, 0, 0.05);
}

.user-avatar {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  font-weight: 700;
  font-size: 16px;
  color: rgba(255, 255, 255, 0.9);
  background: linear-gradient(135deg, rgb(59, 130, 246), rgb(37, 99, 235));
  cursor: pointer;
  box-shadow: 0 4px 16px rgba(59, 130, 246, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.3),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

/* Glossy highlight on avatar */
.user-avatar::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 50%;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.3) 0%, transparent 100%);
  pointer-events: none;
}

.user-avatar:hover {
  transform: translateY(-2px) scale(1.05);
  box-shadow: 0 8px 24px rgba(59, 130, 246, 0.4),
              inset 0 1px 0 rgba(255, 255, 255, 0.4),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

.user-avatar:active {
  transform: translateY(0) scale(1);
  box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.3),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

/* Dark Mode */
:global(.dark) .navbar-island {
  background: rgba(20, 20, 20, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4),
              inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

:global(.dark) .navbar-island::before {
  opacity: 0.2;
}

:global(.dark) .logo-text {
  color: #fff;
}

:global(.dark) .chat-title {
  color: #fff;
}

:global(.dark) .icon-btn {
  background: rgba(0, 0, 0, 0.15);
  color: #fff;
  border: 2px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2),
              inset 0 1px 0 rgba(255, 255, 255, 0.15),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

:global(.dark) .icon-btn::before {
  opacity: 0.4;
}

:global(.dark) .icon-btn:hover {
  background: rgba(0, 0, 0, 0.25);
  border-color: rgba(255, 255, 255, 0.4);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3),
              inset 0 1px 0 rgba(255, 255, 255, 0.2),
              inset 0 -1px 0 rgba(0, 0, 0, 0.2);
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .navbar-container {
    top: 12px;
    left: 68px; /* Adjust for mobile panel button position (12px + 40px + 16px gap) */
    right: 12px;
  }

  .navbar-container.with-panel {
    left: 316px; /* Left panel width (300px) + 16px gap */
  }

  .navbar-island {
    padding: 10px 16px;
    border-radius: 16px;
  }

  .navbar-content {
    gap: 12px;
  }

  .logo-text {
    font-size: 18px;
  }

  .logo-image {
    width: 28px;
    height: 28px;
    object-fit: contain;
  }

  .chat-title {
    font-size: 14px;
  }

  .icon-btn {
    width: 32px;
    height: 32px;
  }

  .user-avatar {
    width: 32px;
    height: 32px;
    font-size: 14px;
  }
}

@media (max-width: 480px) {
  .navbar-content {
    gap: 8px;
  }

  .logo-section {
    gap: 6px;
  }

  .logo-text {
    display: none;
  }

  .chat-title {
    font-size: 13px;
  }
}
</style>


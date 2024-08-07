// import Aura from '@primevue/themes/aura'
import MainPreset from './presets/main'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },

  css: ['~/assets/css/main.css',
    'primeicons/primeicons.css',
    'primeflex/primeflex.css'
  ],

  modules: [
    '@primevue/nuxt-module'
  ],

  primevue: {
    options: {
        theme: {
            preset: MainPreset,
            options: {
              prefix: 'ex',
              darkModeSelector: '.ex-app-dark'
          }
        }
    }
},

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {}
    }
  }
})

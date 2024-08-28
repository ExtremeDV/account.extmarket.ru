/** @type {import('tailwindcss').Config} */
const primeui = require('tailwindcss-primeui')
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {},
  },
  darkMode: ['selector', '[class="p-dark"]'],
  lugins: [primeui]
}


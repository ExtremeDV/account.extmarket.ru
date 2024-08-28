<template>
  <div>
    <Button label="Toggle Color Scheme" @click="toggleColorScheme()" />
    <NuxtPage />
  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    toggleColorScheme() {
      const element = document.querySelector('html')
      document.documentElement.classList.toggle('ex-app-dark')
    },
  },
}
</script>

<template>
  <Header />

  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/courses">Courses</RouterLink>
    <RouterLink to="/profile">Profile</RouterLink>
  </nav>

  <RouterView />
</template>

<script setup>
import Header from './components/Header.vue'
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
nav {
  background-color: #f4f4f4;
  padding: 15px;
}

nav a {
  margin-right: 15px;
  text-decoration: none;
  color: black;
}

nav a.router-link-active {
  color: #42b983;
  font-weight: bold;
}
</style>
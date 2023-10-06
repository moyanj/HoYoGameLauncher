<template>
  <div class="app">
    <SideBar />
    <div class="router">
      <router-view />
    </div>
  </div>
</template>

<script setup lang="ts">
import SideBar from "./components/app/SideBar.vue";
</script>

<style scoped>
.app {
  display: flex;
  flex-direction: row;
  height: 100vh;
}

.router {
  flex: 1;
  overflow-y: auto;
}
</style>

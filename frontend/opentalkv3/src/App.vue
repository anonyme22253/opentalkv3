<script setup>
import { useRoute } from 'vue-router'
import sidebar from './components/sidebar.vue'
import navbar from './components/navbar.vue'
import conversation_place from './components/conversation_place.vue'

const route = useRoute()
</script>

<template>


  <router-view v-if="route.path === '/login' || route.path === '/register'" />

  <div v-else class="chat-app">
    <navbar />
    <div class="chat-content">
    <sidebar  @selected-user="selected_user = $event"/>
    <conversation_place :selected_user="selected_user" />
    </div> 
  </div>

</template>
<script scoped >
import {ref} from 'vue'
const selected_user=ref(null)

</script>
<style>
.chat-app {
  width: 100%;
  height: 100vh;
}

.chat-content {
  display: flex;
  width: 100%;
  height: calc(100vh - 70px);
}
</style>

<template>
  <aside class="sidebar">
    <div class="sidebar-header">
      <h2>Users</h2>
    </div>

    <div class="user-container">
      <div class="user" v-for="user in users_list" :key="user.id || user.email"  @click="selectuser(user)">
        <div class="image"></div>

        <div class="user-content">
          <div class="text">
            <span class="name">{{user.username}}</span>
            <p class="username">{{user.email}}</p>
          </div>

          <span class="status"></span>
        </div>
      </div>
    </div>
  </aside>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
const user_selected=ref([])
const users_list = ref([])
const emit =defineEmits(['selected-user'])
const users_infos=async()=>{
  try{
    const response= await axios.get('https://fantastic-space-potato-4qgxjrvgprq537xr6-8000.app.github.dev/add_user_to_sidebar/',
            {
                withCredentials: true
            })
            users_list.value=response.data
      


  }catch(error){
    console.log("message:",error)
  }
  
}
const selectuser=(user)=>{
  emit('selected-user', user)

  
}

onMounted(() => {
  users_infos()
  
  
})

</script>

<style scoped>
.sidebar {
  width: 320px;
  height: calc(100vh - 70px);
  background: #0b0f14;
  border-right: 1px solid #1d2733;
  display: flex;
  flex-direction: column;
}

.sidebar-header {
  padding: 20px;
  border-bottom: 1px solid #1d2733;
}

.sidebar-header h2 {
  margin: 0;
  color: #2196f3;
  font-size: 22px;
  font-weight: 700;
}

.user-container {
  padding: 10px 0;
  overflow-y: auto;
}

.user {
  display: flex;
  align-items: center;
  padding: 12px 18px;
  cursor: pointer;
  transition: 0.2s;
}

.user:hover {
  background: #111923;
}

.image {
  width: 48px;
  height: 48px;
  min-width: 48px;
  border-radius: 50%;
  margin-right: 14px;
  background: linear-gradient(
    135deg,
    #2196f3,
    #0d47a1
  );
}

.user-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.text {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.name {
  color: #ffffff;
  font-size: 15px;
  font-weight: 600;
}

.username {
  margin: 0;
  color: #7d8a99;
  font-size: 13px;
}

.status {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #22c55e;
  box-shadow: 0 0 6px #22c55e;
}
</style>
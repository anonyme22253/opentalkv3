import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import signup from './templates/signup.vue'
import login from './templates/login.vue'
import { createWebHistory, createRouter } from 'vue-router'


const routes = [
  { path: '/app', component:App },
  { path: '/register', component:signup },
  { path: '/login', component:login },
  {path:'/', redirect:'/register'},
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})
createApp(App).use(router).mount('#app')

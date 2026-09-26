
<template>
<div class="form-container">
  <form class="form" @submit.prevent="send_login_infos">
      <p class="title">Login</p>
      <p class="message">Welcome back! Please login to your account.</p>

      <label>
          <input class="input" type="email" placeholder="" required v-model="email">
          <span>Email</span>
      </label>

      <label>
          <input class="input" type="password" placeholder="" required v-model="password">
          <span>Password</span>
      </label>

      <div class="options">
          <label class="remember">
              <input type="checkbox">
              <span>Remember me</span>
          </label>
          <a href="#" class="forgot">Forgot password?</a>
      </div>

      <button class="submit">Login</button>

      <p class="signin">
        Don't have an account ?
        <router-link to="/register">Signup</router-link>
      </p>
  </form>
</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import {useRouter} from 'vue-router'
const email = ref('')
const password = ref('')
const csrfToken = ref('')
const router=useRouter()
const get_csrf = async () => {
    try {
        const csrf_response = await axios.get(
            'https://fantastic-space-potato-4qgxjrvgprq537xr6-8000.app.github.dev/get_csrf_token/',
            {
                withCredentials: true
            }
        )

        csrfToken.value = csrf_response.data.csrfToken

        console.log('CSRF:', csrfToken.value)
    } catch (error) {
        console.log('CSRF error:', error)
    }
}

onMounted(() => {
    get_csrf()
})

const send_login_infos = async () => {

    if (!csrfToken.value) {
        console.log('CSRF token is not ready')
        return
    }

    const infos = {
        email: email.value,
        password: password.value
    }

    try {
        const response = await axios.post(
            'https://fantastic-space-potato-4qgxjrvgprq537xr6-8000.app.github.dev/user_login/',
            infos,
            {
                headers: {
                    'X-CSRFToken': csrfToken.value
                },
                withCredentials: true
            }
        )


        router.push('/app')

    } catch (error) {
        console.log('message:', error)
    }
}
</script>

<style scoped>
:global(html), :global(body) {
  margin: 0;
  padding: 0;
  min-height: 100%;
  width: 100%;
  background: #0a0a0f;
}

:global(#app) {
  margin: 0;
  padding: 0;
  max-width: 100%;
  width: 100%;
  min-height: 100vh;
  background: #0a0a0f;
}

.form-container {
  min-height: 100vh;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: radial-gradient(circle at 20% 20%, rgba(0, 191, 255, 0.08), transparent 40%),
              radial-gradient(circle at 80% 80%, rgba(138, 43, 226, 0.08), transparent 40%),
              #0a0a0f;
  padding: 20px;
  box-sizing: border-box;
}

.form {
  width: 100%;
  max-width: 400px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  padding: 40px 36px;
  border-radius: 20px;
  background: linear-gradient(145deg, #1a1a22, #16161c);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow:
    0 20px 50px rgba(0, 0, 0, 0.5),
    0 0 0 1px rgba(255, 255, 255, 0.02) inset,
    0 1px 0 rgba(255, 255, 255, 0.05) inset;
  color: #fff;
  box-sizing: border-box;
}

.title {
  margin: 0;
  text-align: center;
  font-size: 30px;
  font-weight: 700;
  background: linear-gradient(90deg, #00bfff, #8a2be2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.message {
  margin: 0 0 10px;
  text-align: center;
  font-size: 14px;
  color: #8b8b93;
  line-height: 1.4;
}

.form label {
  position: relative;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form label span {
  font-size: 12px;
  font-weight: 600;
  color: #9a9aa5;
  letter-spacing: 0.3px;
}

.input {
  width: 100%;
  height: 48px;
  padding: 0 16px;
  box-sizing: border-box;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  outline: none;
  background-color: rgba(255, 255, 255, 0.03);
  color: #fff;
  font-size: 15px;
  transition: all 0.25s ease;
}

.input:hover {
  border-color: rgba(255, 255, 255, 0.2);
  background-color: rgba(255, 255, 255, 0.05);
}

.input:focus {
  border-color: #00bfff;
  background-color: rgba(0, 191, 255, 0.06);
  box-shadow: 0 0 0 3px rgba(0, 191, 255, 0.15);
}

.input::placeholder {
  color: #666;
}

.options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: -6px;
}

.remember {
  display: flex !important;
  flex-direction: row !important;
  align-items: center;
  gap: 6px;
  cursor: pointer;
}

.remember input[type="checkbox"] {
  width: 15px;
  height: 15px;
  accent-color: #00bfff;
  cursor: pointer;
}

.remember span {
  font-size: 13px;
  color: #9a9aa5;
  font-weight: 500;
}

.forgot {
  font-size: 13px;
  color: #00bfff;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.2s ease;
}

.forgot:hover {
  color: #8a2be2;
  text-decoration: underline;
}

.submit {
  width: 100%;
  height: 50px;
  border: none;
  border-radius: 10px;
  background: linear-gradient(90deg, #00bfff, #8a2be2);
  background-size: 200% auto;
  color: #fff;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: all 0.35s ease;
  margin-top: 6px;
  box-shadow: 0 8px 24px rgba(0, 191, 255, 0.25);
}

.submit:hover {
  background-position: right center;
  box-shadow: 0 10px 30px rgba(138, 43, 226, 0.35);
  transform: translateY(-2px);
}

.submit:active {
  transform: translateY(0);
}

.signin {
  margin: 4px 0 0;
  text-align: center;
  font-size: 14px;
  color: #8b8b93;
}

.signin :deep(a) {
  color: #00bfff;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.2s ease;
}

.signin :deep(a:hover) {
  color: #8a2be2;
  text-decoration: underline;
}

@media (max-width: 500px) {
  .form {
    padding: 28px 24px;
  }
}
</style>
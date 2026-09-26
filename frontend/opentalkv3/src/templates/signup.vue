<template>
<div class="form-container">
  <form class="form" @submit.prevent="send_infos">
      <p class="title">Register</p>
      <p class="message">Signup now and get full access to our app.</p>
          <div class="flex">
          <label>
              <input class="input" type="text" placeholder="" required="" v-model="firstname">
              <span>Firstname</span>
          </label>

          <label>
              <input class="input" type="text" placeholder="" required="" v-model="lastname">
              <span>Lastname</span>
          </label>
      </div>  
              
      <label>
          <input class="input" type="email" placeholder="" required="" v-model="email">
          <span>Email</span>
      </label> 
          
      <label>
          <input class="input" type="password" placeholder="" required="" v-model="password">
          <span>Password</span>
      </label>
      <label>
          <input class="input" type="password" placeholder="" required="" v-model="confirm_password">
          <span>Confirm password</span>
      </label>
      <button class="submit">Submit</button>
      <p class="signin">Already have an acount ? <router-link to="/login">Signin</router-link></p>
  </form>
</div>
</template>

<script setup>
import {ref} from 'vue'
import axios from 'axios'
const firstname = ref('')
const lastname =ref('')
const email=ref('')
const password=ref('')
const confirm_password=ref('')
const csrfToken = ref('')
const get_csrf=async()=> {
    try{
        const csrf_response= await axios.get('https://fantastic-space-potato-4qgxjrvgprq537xr6-8000.app.github.dev/get_csrf_token/',{withCredentials:true})
        csrfToken.value = csrf_response.data.csrfToken
    }catch(error){
        console.log('message:', error)
    }
}
get_csrf()
const send_infos=async ()=>{
    if(firstname.value.length===0||lastname.value.length===0){
        alert('first name and last name can not be empty')
    }else if(email.value.length===0){
        alert('email can not be empty')
    }else if(password.value!==confirm_password.value){
        alert('password is incorrect')
    }else{
        const user_infos={
            firstname: firstname.value,
            lastname: lastname.value,
            email: email.value,
            password: password.value
        }
        try{
            const send_respone= await axios.post('https://fantastic-space-potato-4qgxjrvgprq537xr6-8000.app.github.dev/register/',user_infos,{ headers: { 'X-CSRFToken': csrfToken.value }, withCredentials: true})
        }catch(error){
            console.log('message :', error)
        }
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

.flex {
  display: flex;
  gap: 12px;
  width: 100%;
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

  .flex {
    flex-direction: column;
    gap: 18px;
  }
}
</style>
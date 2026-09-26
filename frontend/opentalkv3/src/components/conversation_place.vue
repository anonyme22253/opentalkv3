<template>
  <!-- From Uiverse.io by ahmed150up --> 
<div class="card-container">
  <div class="card-header">
    <div class="img-avatar"></div>
    <div class="text-chat">Chat</div>
  </div>
  <div class="card-body">
    <div class="messages-container">
        <div class="message-box left">
            <p></p>
        </div>
        <div class="message-box right">
            <p></p>
        </div>
    </div>
    <div class="message-input">
      <form>
        <textarea placeholder="Type your message here" class="message-send"></textarea>
        <button type="submit" class="button-send">Send</button>
      </form>
    </div>
  </div>
</div>


</template>
<style scoped>
.card-container {
  background-color: #111923;
  border: 1px solid #1d2733;
  border-radius: 10px;
  margin: 20px;
  display: flex;
  flex-direction: column;
  flex: 1;
  min-width: 0;
  min-height: 0;
  overflow: hidden;
}

.card-header {
  display: flex;
  align-items: center;
  padding: 15px 20px;
  border-bottom: 1px solid #1d2733;
  background-color: #0b0f14;
}

.card-header .img-avatar {
  width: 45px;
  height: 45px;
  min-width: 45px;
  border-radius: 50%;
  margin-right: 15px;
  background: linear-gradient(135deg, #2196f3, #0d47a1);
}

.card-header .text-chat {
  color: #ffffff;
  margin: 0;
  font-size: 18px;
  font-weight: 600;
}

.card-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 0;
}

.messages-container {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.message-box {
  max-width: 60%;
  padding: 10px 14px;
  border-radius: 12px;
  margin: 0;
}

.message-box p {
  margin: 0;
  font-size: 14px;
}

.message-box.left {
  align-self: flex-start;
  background-color: #1d2733;
  color: #ffffff;
}

.message-box.right {
  align-self: flex-end;
  background-color: #2196f3;
  color: #ffffff;
}

.message-input {
  padding: 15px;
  border-top: 1px solid #1d2733;
  background-color: #0b0f14;
}

.message-input form {
  display: flex;
  align-items: center;
  gap: 10px;
}

.message-input .message-send {
  flex: 1;
  height: 45px;
  padding: 10px 15px;
  border: 1px solid #1d2733;
  border-radius: 10px;
  resize: none;
  background-color: #111923;
  color: #ffffff;
  outline: none;
  font-size: 14px;
}

.message-input .message-send::placeholder {
  color: #7d8a99;
}

.message-input .message-send:focus {
  border-color: #2196f3;
}

.message-input .button-send {
  height: 45px;
  padding: 0 20px;
  border: none;
  border-radius: 10px;
  background-color: #2196f3;
  color: #ffffff;
  cursor: pointer;
  font-size: 14px;
  transition: 0.2s;
}

.message-input .button-send:hover {
  background-color: #1976d2;
}
</style>
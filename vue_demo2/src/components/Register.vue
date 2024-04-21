<template>
    <div class="registration-form">
      <h2>用户注册</h2>
      <form @submit.prevent="register" class="form">
        <div class="form-group">
          <label for="username">用户名</label>
          <input type="text" id="username" v-model.trim="username" required>
        </div>
        <div class="form-group">
          <label for="email">邮箱</label>
          <input type="email" id="email" v-model.trim="email" required>
        </div>
        <div class="form-group">
          <label for="password">密码</label>
          <input type="password" id="password" v-model.trim="password" required>
        </div>
        <button type="submit" class="btn-register">注册</button>
      </form>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  import axios from 'axios';
  
  const username = ref('');
  const email = ref('');
  const password = ref('');
  let errorMessage = '';
  
  const register = async () => {
    try {
      const response = await axios.post('http://localhost:8000/register/', {
        username: username.value,
        email: email.value,
        password: password.value
      });
      // 如果注册成功，你的 API 可能会返回一些用户信息或者 token，你可以根据实际情况处理返回的数据
      console.log('注册成功，返回的数据:', response.data);
      // 清空表单数据
      username.value = '';
      email.value = '';
      password.value = '';
      // 清空错误信息
      errorMessage = '';
    } catch (error:any) {
      // 处理注册失败的情况
      if (error.response) {
        // 请求已发出，但服务器响应的状态码不在 2xx 范围内
        console.error('注册失败，服务器响应错误:', error.response.data);
        errorMessage = '注册失败，请稍后重试';
      } else if (error.request) {
        // 请求已发出，但没有收到响应
        console.error('注册失败，未收到服务器响应:', error.request);
        errorMessage = '注册失败，请检查网络连接';
      } else {
        // 设置请求时发生错误
        console.error('注册失败，请求错误:', error.message);
        errorMessage = '注册失败，请稍后重试';
      }
    }
  };
  </script>
  
  <style scoped>
  .registration-form {
    max-width: 400px;
    margin: 0 auto;
  }
  
  .form {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 5px;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }
  
  .form-group input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ced4da;
    border-radius: 3px;
  }
  
  .btn-register {
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 3px;
    padding: 10px 20px;
    cursor: pointer;
  }
  
  .btn-register:hover {
    background-color: #0056b3;
  }
  
  .error-message {
    color: red;
    margin-top: 10px;
  }
  </style>
  
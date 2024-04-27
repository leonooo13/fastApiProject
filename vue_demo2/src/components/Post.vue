<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { useRoute } from 'vue-router';
  
  interface Post {
    id: number;
    title: string;
    content: string;
    modified_date: string;
  }
  
  const post = ref<Post>({
    id: 0,
    title: '',
    content: '',
    modified_date: ''
  });
  
  const fetchPost = async (postId: number) => {
    try {
      const response = await axios.get(`http://localhost:8000/post/${postId}`);
      post.value = response.data.data;
    } catch (error) {
      console.error('请求帖子时出错:', error);
    }
  };
  
  // 使用 useRoute 获取当前路由的参数
  const route = useRoute();
  const postId = parseInt(route.params.id as string);
  
  // 在组件挂载后立即调用 fetchPost 方法
  onMounted(() => {
    fetchPost(postId);
  });
  </script>

<template>
    <div class="post">
      <div class="nav"> 
        <router-link to="/" class="back-link">返回首页</router-link>
      </div>
      <div class="header">
        <h2>{{ post.title }}</h2>
        <div class="date">{{ post.modified_date }}</div>
      </div>
      <div class="content">{{ post.content }}</div>
    </div>
  </template>
  
<style scoped>
  .post {
    position: relative; /* 将 .nav 设置为相对定位的参考点 */
    width: 100%;
    max-width: 800px; /* 设置最大宽度 */
    margin: 0 auto; /* 居中显示 */
    padding: 20px;
    min-height: 500px;
  }
  
  .nav {
    position: absolute; /* 绝对定位 */
    top: 1px; /* 距离顶部 */
    left: 1px; /* 距离左侧 */
  }
  
  .header {
    display: flex;
    justify-content: space-between; /* 让标题、日期和返回链接在头部水平排列 */
    align-items: center; /* 让标题、日期和返回链接在头部垂直居中 */
  }
  
  .back-link {
    color: #007bff;
    text-decoration: none;
  }
  
  .date {
    font-style: italic; /* 设置日期部分为斜体 */
  }
  
  .content {
    margin-top: 20px; /* 调整内容部分的顶部间距 */
  }
</style>

  

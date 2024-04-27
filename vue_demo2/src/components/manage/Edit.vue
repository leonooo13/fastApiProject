<template>
    <div class="home">
      <h3>主页展示</h3>
      <div class="article-list">
        <ul>
          <li v-for="post in data" :key="post.id" class="article-item">
            <div class="post-info">
              <div class="title_id">{{ post.id }}</div>
              <router-link :to="'/post/' + post.id" class="title-link">{{ post.title }}</router-link>
              <div class="date">{{ post.date }}</div>
              <div class="button-group">
                <button @click="editPost(post.id)" class="edit-button">修改</button>
                <button @click="deletePost(post.id)" class="delete-button">删除</button>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  interface Post {
    id: number;
    title: string;
    content: string;
    date: string;
  }
  
  const data = ref<Post[]>([]);
  
  const fetchData = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/posts/`);
      data.value = response.data.data;
    } catch (error) {
      console.error('请求数据时出错:', error);
    }
  };
  
  // 在组件挂载后立即调用 fetchData 方法
  onMounted(fetchData);
  
  // 修改文章的函数
  const editPost = async (postId: number) => {
    try{
      await axios.put(`http://127.0.0.1:8000/posts/${postId}`)
    }
    catch (error){
      console.error(error)
    }
  };
  
  // 删除文章的函数
  const message = ref()
  const deletePost = async(post_id: number) => {
    // 实现删除文章的逻辑
    console.log(post_id)
    try {
     const resp = await axios.delete(`http://127.0.0.1:8000/posts/delete/${post_id}`)
     message.value = resp.data.data
     console.log(message.value)
     if( message.value =="delete post success"){
       alert("删除成功")
       fetchData();
     }

    
    }
      catch (error) {
    console.error(error)
      
    }
    };
  </script>
  
  <style scoped>
  .home {
    max-width: 800px;
    margin: 0 auto;
  }
  
  .article-list {
    margin-top: 20px;
  }
  
  .article-item {
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  .post-info {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .title_id {
    font-weight: bold;
    margin-right: 10px;
  }
  
  .title-link {
    color: #007bff;
    text-decoration: none;
  }
  
  .date {
    color: #888;
  }
  
  .button-group {
    display: flex;
    align-items: center;
  }
  
  .edit-button,
  .delete-button {
    margin-left: 10px;
    padding: 5px 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 3px;
    cursor: pointer;
  }
  
  .edit-button:hover,
  .delete-button:hover {
    background-color: #0056b3;
  }
  </style>
  
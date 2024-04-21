<template>
  <div class="home">
    <h3>主页展示</h3>
    <div class="article-list">
      <ul>
        <li v-for="post in data" :key="post.id" class="article-item">
          <div class="post-info">
            <div class="title_id">{{ post.id }}</div>
            <router-link :to="'/post/' + post.id" class="title-link">
              {{ post.title }}
            </router-link>
            <div class="date">{{ post.date }}</div>
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
    const response = await axios.get('http://localhost:8000/posts/');
    data.value = response.data.data;
  } catch (error) {
    console.error('请求数据时出错:', error);
  }
};

// 在组件挂载后立即调用 fetchData 方法
onMounted(fetchData);
</script>

<style scoped>
.home {
  width: 100%;
  max-width: 800px; /* 设置最大宽度 */
  margin: 0 auto; /* 居中显示 */
  padding: 20px;
}

.article-list {
  margin-top: 20px;
}

.article-item {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  margin-bottom: 10px;
  list-style-type: none; /* 去掉小黑点 */
}

.post-info {
  display: flex; /* 使用 Flexbox 布局 */
  align-items: center; /* 垂直居中对齐 */
  justify-content: space-between; /* 平均分布子元素并右对齐 */
}

.title_id {
  font-size: 14px; /* 缩小 ID 字体 */
  color: #666; /* 变浅颜色 */
}

.title-link {
  font-size: 18px;
  font-weight: bold;
  color: #333;
  text-decoration: none; /* 去除下划线 */
  transition: color 0.3s; /* 添加过渡效果 */
}

.title-link:hover {
  color: #007bff; /* 鼠标悬停时改变颜色 */
}

.date {
  font-size: 14px; /* 缩小日期字体 */
  color: #999; /* 变浅颜色 */
}
</style>

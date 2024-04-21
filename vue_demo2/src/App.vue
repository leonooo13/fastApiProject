<template>
  <div class="contain">
    <div class="nav">
      <router-link to="/" class="nav-link">首页</router-link>
      <router-link to="/login" class="nav-link">登录</router-link>
      <router-link to="/register" class="nav-link">注册</router-link>
      <router-link to="/manage" class="nav-link">管理</router-link>
    </div>
    <div class="content">
    <router-view/>
    </div>
    <div class="foot">
    <Footer/>
    </div>
  </div>
</template>

<script setup name="App" lang="ts">
import Footer from "@/components/Footer.vue"

</script>

<style scoped>
.contain{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 100vh;
  
}
.nav {
  background-color: #676869; /* 浅灰色背景 */
  padding: 10px; /* 顶部和底部留出一些空间 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 轻微的阴影效果 */
  display: flex;
  justify-content: flex-end;
  border-radius: 10px;
}

.nav-link {
  color: #e8e5e5; /* 导航链接颜色 */
  text-decoration: none; /* 去掉下划线 */
  font-weight: bold; /* 加粗字体 */
  transition: color 0.3s; /* 鼠标悬停时颜色过渡 */
  padding-right: 30px;
}

.nav-link:not(:last-child) {
  margin-right: 20px; 
}

.nav-link:hover {
  color: #007bff; /* 鼠标悬停时的链接颜色 */
}
.content{
  font-family: 'fangsong';
  display: flex;
  justify-content: center;
}
.foot{
  display: flex;
  justify-content: center;
  align-self: center;
  margin-top: 10px;
  color: white;
  border: #007bff;
  border-radius: 20px;
  width: 200px;
  align-content: center;
  background-color: black;
}
</style>

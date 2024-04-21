<template>
    <div class="article-links">
      <router-link to="/manage/new" class="button">新增文章</router-link>
      <router-link to="/manage/edit/" class="button">编辑文章</router-link>
    </div>
  </template>
  
  <style scoped>
  .article-links {
    margin-bottom: 20px;
  }
  
  .button {
    display: inline-block;
    padding: 10px 20px;
    margin-right: 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    text-decoration: none;
    cursor: pointer;
  }
  
  .button:hover {
    background-color: #0056b3;
  }
  </style>
  
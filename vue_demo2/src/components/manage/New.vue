<template>
  <div class="article-editor">
    <form @submit.prevent="submitArticle" class="form">
      <div class="form-group">
        <label for="title" class="form-label">标题</label>
        <input type="text" id="title" v-model="article.title"  required class="form-input">
      </div>

      <div class="form-group">
        <label for="content" class="form-label">内容</label>
        <textarea id="content"  v-model="article.content" rows="10" required class="form-textarea"></textarea>
      </div>
      
      <button type="submit" class="publish-button">发布</button>
    </form>
    <SuccessMessage v-if="message"/>
  </div>
  
</template>

<script setup lang="ts">
import { ref, watch, onMounted} from 'vue';
import axios from 'axios';
import SuccessMessage from '@/components/Tips/SuccessMessage.vue';
import { useRoute } from 'vue-router';

interface Article {
  title: string;
  content: string;
}

const article = ref<Article>({
  title: '',
  content: ''
});

const message = ref(false);

const route = useRoute();
const postId = ref(route.params.id);

const addArticle = () => {
  axios.post('http://127.0.0.1:8000/post/new/', article.value)
    .then(response => {
      if (response.data.code == 200) {
        message.value = true;
        article.value.title = '';
        article.value.content = '';
        setTimeout(() => {
          message.value = false;
        }, 3000);
      }
    })
    .catch(error => {
      console.error('提交失败:', error);
    });
};

const editArticle = () => {
  axios.put(`http://127.0.0.1:8000/post/new/${postId.value}`, article.value)
    .then(response => {
      if (response.data.code == 200) {
        message.value = true;

        article.value.title = '';
        article.value.content = '';
        setTimeout(() => {
          message.value = false;
        }, 3000);
      }
    })
    .catch(error => {
      console.error('提交失败:', error);
    });
};

const submitArticle = () => {
  if (postId.value) {
    editArticle();
  } else {
    addArticle();
  }
};

const fetchArticle = () => {
  const postId = route.params.id;
  if (postId) {
    axios.get(`http://127.0.0.1:8000/post/${postId}`)
      .then(response => {
        const data = response.data.data;
        article. value.title = data.title;
        article.value.content = data.content;
        console.log(data)
      })
      .catch(error => {
        console.error('获取文章失败:', error);
      });
  }
};

onMounted(() => {
  fetchArticle();
});

watch(() => route.params.id, (newId) => {
  postId.value = newId;
});
</script>

<style scoped>
.article-editor {
  width: 80%;
  margin: 0 auto;
  background-color: rgb(229, 227, 221);
  padding: 2rem;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-label {
  font-weight: bold;
  margin-bottom: 0.5rem;
  display: block;
}

.form-input,
.form-textarea {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.form {
  display: flex;
  flex-direction: column;
}

.publish-button {
  padding: 0.5rem 1rem;
  font-size: 1rem;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 1rem;
  align-self: flex-end; /* 右对齐 */
}

.publish-button:hover {
  background-color: #0056b3;
}
</style>

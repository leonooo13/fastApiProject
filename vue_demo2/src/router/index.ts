import { createRouter, createWebHistory } from "vue-router";
import Register from "@/components/Register.vue"
import Login from "@/components/Login.vue"
import Home from "@/components/Home.vue"
import News from "@/components/News.vue";
import Manage from "@/components/Manage.vue";
import New from "@/components/manage/New.vue";
import Edit from "@/components/manage/Edit.vue";
import Post from "@/components/Post.vue";
const router = createRouter({
    history:createWebHistory(),
    routes:[
        {
            path:'/',
            component:Home,
            name:'Home'
        },
        {
            path:'/login',
            component:Login,
            name:'Login',
        },
        {
            path:'/register',
            component:Register,
            name:'Register',
        },
        {
            path:'/news',
            component:News,
            name:'News',
        },
        {
            path: '/manage',
            component:Manage,
            name: 'Manage',
        },
        {
            path: '/post/:id',
            component:Post,
            name: 'Post',
        },
        {
            path:'/manage/new/:id',
            component: New,
            name:'EditArticle',
        },
        {
            path:'/manage/new',
            component: New,
            name:'New',
        },
        {
            path:'/manage/edit/',
            component: Edit,
            name:'Edit',
        }
    ]
})

export default router
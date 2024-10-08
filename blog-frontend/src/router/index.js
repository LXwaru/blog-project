import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ListUsers from '../views/ListUsers.vue'
import ListBlogsByUser from '@/views/ListBlogsByUser.vue'
import DetailBlog from '@/views/DetailBlog.vue'
import CreateAccount from '../views/CreateAccount.vue'
import ListMyBlogs from '../views/ListMyBlogs.vue'
import CreateBlog from '../views/CreateBlog.vue'
import Navigation from '../components/Navigation.vue'
import ListBlogs from '../views/ListBlogs.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/ListUsers',
      name: 'ListUsers',
      component: ListUsers
    },
    {
      path: '/listBlogsByUser/:userId',
      name: 'listBlogsByUser',
      component: ListBlogsByUser,
      props: true
    },
    {
      path: '/DetailBlog/:itemId',
      name: 'DetailBlog',
      component: DetailBlog,
      props: true
    },
    {
      path: '/CreateAccount',
      name: 'CreateAccount',
      component: CreateAccount
    },
    {
      path: "/ListMyBlogs",
      name: "ListMyBlogs",
      component: ListMyBlogs,
      props: true
    },
    {
      path: "/CreateBlog",
      name: "CreateBlog",
      component: CreateBlog
    },
    {
      path: '/Navigation',
      name: 'Navigation',
      component: Navigation
    },
    {
      path: "/ListBlogs",
      name: "ListBlogs",
      component: ListBlogs,
      props: true
    }
  ]
})

export default router

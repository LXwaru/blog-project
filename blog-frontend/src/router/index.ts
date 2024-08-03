import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ListUsers from '../views/ListUsers.vue'
import ListBlogsByUser from '@/views/ListBlogsByUser.vue'

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
    }
  ]
})

export default router

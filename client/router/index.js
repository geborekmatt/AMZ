
import { createRouter, createWebHistory } from 'vue-router'
import matt from '../src/components/matt.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'matt',
      component: matt,
    }
  ]
})

export default router


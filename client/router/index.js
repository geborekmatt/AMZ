HelloWorld
import { createRouter, createWebHistory } from 'vue-router'
import matt from '../src/components/matt.vue'
import HelloWorld from '../src/components/HelloWorld.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'matt',
      component: matt,
    },
    {
      path: '/hw',
      name: 'HelloWorld',
      component: HelloWorld,
    }
  ]
})

export default router


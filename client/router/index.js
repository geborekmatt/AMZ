import { createRouter, createWebHistory } from 'vue-router'
import matt from '../src/components/matt.vue'
import BrandsDashboard from '../src/components/BrandsDashboard.vue'
import HopperDashboard from '../src/components/HopperDashboard.vue'
import ProductsDashboard from '../src/components/ProductsDashboard.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'matt',
      component: matt,
    },
    {
      path: '/hopper',
      name: 'HopperDashboard',
      component: HopperDashboard,
    },
    {
      path: "/brands",
      name: 'BrandsDashboard',
      component: BrandsDashboard,
    },
    {
      path: "/products",
      name: 'ProductsDashboard',
      component: ProductsDashboard,
    }
  ]
})

export default router


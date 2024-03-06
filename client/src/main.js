import { createApp } from 'vue'
import App from './App.vue'
import router from '../router'
import PrimeVue from 'primevue/config';
import axios from 'axios'
//PrimeVue Component Imports
import Button from 'primevue/button';
import MenuBar from 'primevue/MenuBar';
import 'primevue/resources/themes/md-light-indigo/theme.css'
import 'primeicons/primeicons.css'


axios.defaults.baseURL = import.meta.env.VITE_API_TEST

const app = createApp(App)

app.use(router,axios)
app.use(PrimeVue)
app.component('Button', Button)
app.component('MenuBar', MenuBar)
app.mount('#app')

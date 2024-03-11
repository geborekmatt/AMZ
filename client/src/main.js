import { createApp } from 'vue'
import App from './App.vue'
import router from '../router'
import PrimeVue from 'primevue/config';
import axios from 'axios'
//PrimeVue Component Imports
import Button from 'primevue/button';
import MenuBar from 'primevue/menubar';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';   // optional
import Row from 'primevue/row';                   // optional
import InputText from 'primevue/inputtext';
import InputSwitch from 'primevue/inputswitch';
import Dialog from 'primevue/dialog';
import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice';

import 'primevue/resources/themes/md-light-indigo/theme.css'
import 'primeicons/primeicons.css'
import 'primevue/resources/primevue.min.css';
import 'primeflex/primeflex.css';


axios.defaults.baseURL = import.meta.env.VITE_API_TEST

const app = createApp(App)

app.use(router,axios)
app.use(PrimeVue)
app.use(ToastService)
app.component('Button', Button)
app.component('MenuBar', MenuBar)
app.component('DataTable', DataTable)
app.component('Column', Column)
app.component('ColumnGroup', ColumnGroup)
app.component('Row', Row)
app.component('InputText', InputText)
app.component('InputSwitch', InputSwitch)
app.component('Dialog', Dialog)
app.component('Toast', Toast)
app.mount('#app')

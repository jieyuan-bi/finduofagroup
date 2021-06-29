import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus';
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'element-plus/lib/theme-chalk/index.css';
import 'mdb-vue-ui-kit/css/mdb.min.css';

axios.defaults.baseURL = 'http://192.168.0.209:8000'
axios.defaults.timeout = 3000
// axios.defaults.baseURL = 'http://localhost:8000'

const app = createApp(App)
app.use(store)
app.use(router, axios)
app.use(ElementPlus)
app.mount('#app')

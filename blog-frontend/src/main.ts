import './assets/main.css'

import { createApp } from 'vue'
import store from './store'
import App from './App.vue'
import router from './router'

const app = createApp(App)


createApp(App)
.use(router)
.use(store)
.mount('#app')

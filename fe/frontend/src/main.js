// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import {mavonEditor} from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import axios from 'axios'
Vue.use(ElementUI)
Vue.use(mavonEditor)
Vue.config.productionTip = false
axios.defaults.baseURL = 'http://150.158.168.151:9000/'
Vue.prototype.$axios = axios
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})

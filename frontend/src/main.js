import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueResource from 'vue-resource'
import VueCharts from 'vue-charts'
import { store } from './store/store.js'

Vue.use(VueResource)
Vue.use(VueCharts)

window._ = require('lodash');

Vue.http.options.root = RESOURCE_URL.slice(0,-1)

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})

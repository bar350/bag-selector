import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueResource from 'vue-resource'
import VueCharts from 'vue-charts'
import { store } from './store/store.js'

// Load the Vue Resource and Vue Charts libraries into the main vue instance
Vue.use(VueResource)
Vue.use(VueCharts)

// Load lodash into the window object
window._ = require('lodash');

// set the base resource url
Vue.http.options.root = RESOURCE_URL.slice(0,-1)

// Start the main vue instance
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})

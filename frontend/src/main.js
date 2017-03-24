import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueResource from 'vue-resource'
import VueCharts from 'vue-charts'

Vue.use(VueResource)
Vue.use(VueCharts)

window._ = require('lodash');

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})

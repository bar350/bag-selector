import Vue from 'vue'
import Router from 'vue-router'
import Filtering from '../components/Filtering.vue'
import GameDetail from '../components/GameDetail.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'gameFilter',
      component: Filtering
    },
    {
      path: '/game/:id', 
      component: GameDetail, 
      name: "gameDetail" 
    }
  ]
})

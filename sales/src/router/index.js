import Vue from 'vue'
import Router from 'vue-router'
import index from '@/page/index.vue'

Vue.use(Router)

export default new Router({
  // nginx 配置2
  base: '/story/',
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    }
  ]
})

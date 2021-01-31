import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/views/layout'
import First from '@/components/first'
import User from '@/components/user'
import ItemsFee from '@/components/decoration'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Layout',
      component: Layout,
      children: [{
        path: '/',
        name: 'First',
        component: First
      },
      {
        path: '/user',
        name: 'User',
        component: User
      },
      {
        path: '/decoration',
        name: 'ItemsFee',
        component: ItemsFee
      }
      ]
    }
  ]
})

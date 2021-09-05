import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/views/layout'
import First from '@/components/first'
import User from '@/components/user'
import ItemsFeeA from '@/components/decoration'
import Blog from '@/components/blog'
import Post from '@/components/post'
import Login from '@/components/login'
import Register from '@/components/register'
import Article from '@/components/article'

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
        path: '/register',
        name: 'Register',
        component: Register
      },
      {
        path: '/login',
        name: 'Login',
        component: Login
      },
      {
        path: '/user',
        name: 'User',
        component: User
      },
      {
        path: '/decoration',
        name: 'ItemsFeeA',
        component: ItemsFeeA
      },
      {
        path: '/blog',
        name: 'Blog',
        component: Blog
      },
      {
        path: '/post',
        name: 'Post',
        component: Post
      },
      {
        path: '/article',
        name: 'Article',
        component: Article
      },
      ]
    }
  ]
})

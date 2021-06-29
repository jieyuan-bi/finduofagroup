import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import User from '../views/User.vue'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import Manage from '../views/Manage.vue'

const routes = [
  {
    path: '/home/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/:subject',
    name: 'Subject',
    component: Home,
    // children: [
    //   // UserHome will be rendered inside User's <router-view>
    //   // when /user/:id is matched
    //   { path: '', component: Home },
      
    // ]
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/manage',
    name: 'Manage',
    component: Manage
  },
  {
    path: '/user',
    name: 'User',
    component: User
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

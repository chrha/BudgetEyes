import Vue from 'vue';
import VueRouter from 'vue-router';
import LoginPage from '../account/LoginPage.vue';
import stockPage from '../views/stockpage.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'stockpage',
    component: stockPage,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
  },
];

const router = new VueRouter({
  routes,
});

export default router;

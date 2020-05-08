import Vue from 'vue';
import VueRouter from 'vue-router';
import LoginPage from '../account/LoginPage.vue';
import StockPage from '../views/StockPage.vue';
import BudgetPage from '../views/BudgetPage.vue';
import RegisterPage from '../account/RegisterPage.vue';


Vue.use(VueRouter);

const routes = [
  {
    path: '/stockpage',
    name: 'StockPage',
    component: StockPage,
  },
  {
    path: '/budgetpage',
    name: 'BudgetPage',
    component: BudgetPage,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
    props: true,
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterPage,
  },
];

const router = new VueRouter({
  routes,
});

export default router;

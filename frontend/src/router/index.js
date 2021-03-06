import Vue from 'vue';
import VueRouter from 'vue-router';
import LoginPage from '../account/LoginPage.vue';
import StockPage from '../views/StockPage.vue';
import BudgetPage from '../views/BudgetPage.vue';
import RegisterPage from '../account/RegisterPage.vue';
import ProfilePage from '../account/ProfilePage.vue';
import HomePage from '../home/HomePage.vue';


Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
    props: true,
  },
  {
    path: '/stockpage',
    name: 'StockPage',
    component: StockPage,
  },
  {
    path: '/budgetpage',
    name: 'BudgetPage',
    component: BudgetPage,
    meta: {
      title: 'Budget',
    },
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
    title: 'Login', 
    props: true,
    meta: {
      requiresNotAuth: true,
    },
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterPage,
    meta: {
      requiresNotAuth: true,
    },
  },
  {
    path: '/profile',
    name: 'ProfilePage',
    component: ProfilePage,
    meta: {
      requiresAuth: true,
    },
  },
];

const router = new VueRouter({
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.meta.requiresNotAuth) {
    if (Vue.$cookies.isKey('token')) {
      next({ name: 'BudgetPage' });
    } else {
      next();
    }
  } else if (to.meta.requiresAuth) {
    if (!Vue.$cookies.isKey('token')) {
      next({ name: 'Login' });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;

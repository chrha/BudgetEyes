import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import VueCookies from 'vue-cookies';
import * as Sentry from '@sentry/browser';
import { Vue as VueIntegration } from '@sentry/integrations';
import VueGoogleCharts from 'vue-google-charts';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VueCookies);
Vue.use(VueGoogleCharts);
Vue.$cookies.config('1d');


Sentry.init({
  dsn: 'https://b0ffa0f2093349d2bcdb5dd1d8115cc5@o321568.ingest.sentry.io/5203638',
  integrations: [new VueIntegration({ Vue, attachProps: true })],
});

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');

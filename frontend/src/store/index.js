import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: '',
    username: '',
  },
  mutations: {
    setToken(state, value) {
      /* 
      Sets authentication token which must be used when making requests to api.
      Token is received upon logging in.
      */ 
      state.token = value;
    },
    setUsername(state, name) {
      state.username = name;
    },
  },
  actions: {
  },
  modules: {
  },
});

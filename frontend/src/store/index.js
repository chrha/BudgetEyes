import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    username: '',
    name_and_abbriev: [],
  },
  mutations: {
    setUsername(state, name) {
      state.username = name;
    },
    setStocks(state, stocklist) {
      state.name_and_abbriev = stocklist;
    },
  },
  actions: {
  },
  modules: {
  },
  getters: {
    getUsername: (state) => state.username,
    getStocks: (state) => state.name_and_abbriev,
  },
    
});

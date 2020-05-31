import Vue from 'vue';
import Vuex from 'vuex';
// import axiosInstance from '../ajax/client';


Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    username: '',
    name_and_abbriev: [],
    stockData: {},
    isStockPageMounted: false,
  },
  mutations: {
    setUsername(state, name) {
      state.username = name;
    },
    setStocks(state, stocklist) {
      state.name_and_abbriev = stocklist;
    },
    setStockData(state, payload) {
      state.stockData[payload.key] = payload.data;
    },
    setMounted(state) { 
      state.isStockPageMounted = true;
    },
  },
  actions: {
    /*
    async requestStockData({ state, commit }, payload) {
      axiosInstance.put('stocks/query', { stocks: [payload.abbr], period: payload.period })
        .then((response) => {
          const key = Object.keys(response.data)[0];
          const data = response.data[key];
          commit('setStockData', { key, data });
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => state.stockData[key]
        );
    },
    */
  },
  modules: {
  },
  getters: {
    getUsername: (state) => state.username,
    getStocks: (state) => state.name_and_abbriev,
    getStockDataByAbbr: (state) => (abbr) => state.stockData[abbr],
  },
    
});

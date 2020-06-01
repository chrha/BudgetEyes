import Vue from 'vue';
import Vuex from 'vuex';
import axiosInstance from '../ajax/client';


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
      if (state.stockData[payload.key]) {
        state.stockData[payload.key][payload.period] = payload.data;
      } else {
        state.stockData[payload.key] = {};
        state.stockData[payload.key][payload.period] = payload.data;
      }
    },
    setMounted(state) { 
      state.isStockPageMounted = true;
    },
  },
  actions: {
    async requestStockData({ commit }, payload) {
      let key;
      let periodToStore;
      console.log(payload);
      
      if (!payload.period || payload.period === 7) periodToStore = 'Weekly';
      else if (payload.period === 30) periodToStore = 'Monthly';
      else periodToStore = 'Daily'; 
      return axiosInstance.put('stocks/query/', { stocks: [payload.abbr], period: payload.period })
        .then((response) => {
          [key] = Object.keys(response.data);
          const data = response.data[key];
          commit('setStockData', { key, data, period: periodToStore });
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          throw new Error('No data for this abbriev');
        });
    },
  },
  getters: {
    getUsername: (state) => state.username,
    getStocks: (state) => state.name_and_abbriev,
    getStockDataByAbbr: (state) => ((payload) => {
      if (state.stockData[payload.abbr]) {
        return state.stockData[payload.abbr][payload.period];
      } 
      return {};
    }),
  },
    
});

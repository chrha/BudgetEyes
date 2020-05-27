<template>
  <v-container>
    <div v-if="this.$store.state.username">
      <span> Hey {{ $store.state.username }}! You are following these stocks: </span>
    </div>
    <div v-else-if="user">
      <span> Bye {{ user }}, do come back again! </span>
    </div>
    <div v-else>
      <span> Welcome to BudgetEyes, here is some fucking stock data </span>
    </div>

    <div v-for="(value, key, index) in stocks" :key="index"> 
      <h2> {{ key }} </h2>
      <ul v-for="(value2, key2, index2) in value" :key="index2">
        <h3> {{ key2 }} </h3>
        <li v-for="item in value2" :key="item"> {{item[0]}} - {{item[1]}} </li>
      </ul>
    </div>
  </v-container>
</template>

<script>

import axiosInstance from '../ajax/client';

export default {
  name: 'HomePage',
  props: {
    previous: {
      type: String,
    },
  },
  data() {
    return {
      user: this.previous,
      stocks: {},
    };
  },
  mounted() {
    if (this.$store.state.username) {
      axiosInstance.put('stocks/query/', { period: 10 }, { headers: { Authorization: `Token ${this.$cookies.get('token')}` } })
        .then((response) => {
          this.stocks = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    } else {
      axiosInstance.put('stocks/query/', { stocks: ['MSFT', 'GOOG'], period: 10 })
        .then((response) => {
          const keys = Object.keys(response.data);
          const values = Object.values(response.data);
          for (let i = 0; i < keys.length; i += 1) {
            this.stocks[keys[i]] = values[i];
          }
          this.stocks = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    }
  },
};
</script>

<style>

</style>

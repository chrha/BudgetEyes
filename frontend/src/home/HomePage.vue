<template>
  <v-container fluid id="container"> 
    <div v-if="this.$store.state.username">
      <h3> Hey {{ $store.state.username }}! {{ welcomeMsg }}  </h3>
    </div>
    <div v-else-if="user">
      <h3> Bye {{ user }}, do come back again! </h3>
    </div>
    <div v-else>
      <h3> Welcome to BudgetEyes, here is some stock data </h3>
    </div>
    <v-progress-linear
      color="deep-purple accent-4"
      :active="loading"
      indeterminate
      rounded
      height="6"
    ></v-progress-linear>
    <v-row v-for="(stocklist, key) in stocks" :key="key" class="m-3" 
      style="float:left">
      <StockGraph :stockData="stocklist" :isDaily="false" :stockName="key"/>
    </v-row>
  </v-container>

</template>

<script>
import axiosInstance from '../ajax/client';
import StockGraph from '../stocks/StockGraph.vue';

export default {
  name: 'HomePage',
  props: {
    previous: {
      type: String,
    },
  },
  components: {
    StockGraph,
  },
  data() {
    return {
      user: this.previous,
      stocks: {},
      welcomeMsg: 'Please wait while your stocks are getting loaded:',
      loading: false,
    };
  },
  created() {
    this.loading = true;
    if (this.$store.state.username) {
      axiosInstance.put('stocks/query/', { period: 7 }, { headers: { Authorization: `Token ${this.$cookies.get('token')}` } })
        .then((response) => {
          this.loading = false;
          if (response.status === 204) {
            this.welcomeMsg = 'You are currently not following any stocks, check them out at the stock page!';
          } else {
            this.welcomeMsg = 'You are following these stocks:';
            this.stocks = Object.assign(response.data, this.stocks);
          }
        }).catch((error) => {
          // eslint-disable-next-line
          this.welcomeMsg = 'Something went wrong, how embarrasing!';
          this.loading = false;
          console.log(error);
        });
    } else {
      axiosInstance.put('stocks/query/', { stocks: ['MSFT', 'GOOG', 'AAPL', 'KO', 'AMZN', 'FB'], period: 7 })
        .then((response) => { 
          this.loading = false;
          this.stocks = Object.assign(response.data, this.stocks);
        }).catch((error) => {
          this.welcomeMsg = 'Something went wrong, how embarrasing!';
          this.loading = false;
          // eslint-disable-next-line
          console.log(error);
        });
    }
  },
};

</script>

<style scoped>

</style>

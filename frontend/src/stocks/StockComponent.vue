<template>
<div id="stockpage">
    <v-container id="stock-canvas">
        <v-row v-if="curr_stock">
          <stockGraph 
          :stockData="curr_stock_data" 
          :stockAbbr="curr_stock_abbr" 
          :stockName="curr_stock"
          />
        </v-row>
   </v-container>

</div>
</template>

<script>

import stockGraph from './StockGraph.vue';
import axiosInstance from '../ajax/client';

export default {
  name: 'StockComponent',
  components: {
    stockGraph,
  },
  data() {
    return {
      stocks: [],
      count: 0,
      curr_stock: '',
      curr_stock_data: {},
      curr_stock_abbr: '',

    };
  },
  /**
   * send displayed stock to stocklog.
   * receive chosen dropdown item to display.
   */
  mounted() {
    this.$root.$emit('msg_from_stockcomp', this.curr_stock);
    this.$root.$on('msg_from_stocklog', (value) => {
      console.log('logvalue:', value);
      
      const data = this.$store.getters.getStockDataByAbbr({ abbr: value.abbriev, period: 'Weekly' });
      console.log(data);
      
      if (data && Object.keys(data).length) {
        this.curr_stock_data = data;
      } else {
        axiosInstance.put('stocks/query/', { stocks: [value.abbriev] })
          .then((response) => {
            this.curr_stock_data = response.data[value.abbriev];
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error);
          });
      }
      this.curr_stock_abbr = value.abbriev;
      this.curr_stock = value.name;
    });
    this.$root.$on('msg_from_stocksearch', (value) => {
      [this.curr_stock, this.curr_stock_abbr, this.curr_stock_data] = value;
    });
  },
  methods: {
    /**
     * Triggered by button click & displays next stock in stock list.
     */
    nextStock() {
      if (this.count === this.stocks.length - 1) {
        this.count = 0;
      } else {
        this.count += 1;
      }
      this.curr_stock = this.stocks[this.count];
      this.$root.$emit('msg_from_stockcomp', this.curr_stock);
    },
    /**
     * Triggered by button click & displays previous stock in stock list.
     */
    previousStock() {
      if (this.count === 0) {
        this.count = this.stocks.length - 1;
      } else {
        this.count -= 1;
      }
      this.curr_stock = this.stocks[this.count];
      this.$root.$emit('msg_from_stockcomp', this.curr_stock);
    },
  },
  beforeDestroy() {
    this.$root.$off('msg_from_stocklog');
    this.$root.$off('msg_from_stocksearch');
  },
};
</script>


<style scoped>
    #previousButton{
        background-color: #C7F0DB;
        color: #000000;

    }
    #nextButton{
        background-color: #C7F0DB;
        color: #000000;

    }

</style>

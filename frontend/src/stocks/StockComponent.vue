<template>
<div id="stockpage">
    <b-container id="stock-canvas">
        <b-row>
            <b-col>
              <h1> {{ curr_stock }} </h1>  
            </b-col>

        </b-row>

        <b-row>
            
            <b-col cols >
                <v-btn id= "previousButton" v-on:click="previousStock">Previous</v-btn>
            </b-col>
            
            <b-col cols>
                <v-btn id= "nextButton" v-on:click="nextStock">Next</v-btn>
               
            </b-col>
        </b-row>    
    </b-container>
    
</div>
</template>

<script>


export default {
  name: 'StockComponent',
  data() {
    return {
      stocks: ['stock1',
        'stock2', 
        'stock3', 'stock6'],
      count: 0,
      curr_stock: 'stock1',
    };
  },
  /**
   * send displayed stock to stocklog.
   * receive chosen dropdown item to display.
   */
  mounted() {
    this.$root.$emit('msg_from_stockcomp', this.curr_stock);
    this.$root.$on('msg_from_stocklog', (value) => {
      let exists = false;
      for (let i = 0; i < this.stocks.length; i += 1) {
        if (this.stocks[i] === value) {
          this.count = i;
          this.curr_stock = this.stocks[this.count];
          exists = true;
          break;
        }
      }
      if (!exists) {
        this.stocks.push(value);
        this.count = this.stocks.length - 1;
        this.curr_stock = this.stocks[this.count];
      }
    });
    this.$root.$on('msg_from_stocksearch', (value) => {
      let exists = false;
      for (let i = 0; i < this.stocks.length; i += 1) {
        if (this.stocks[i] === value) {
          this.count = i;
          this.curr_stock = this.stocks[this.count];
          exists = true;
          break;
        }
      }
      if (!exists) {
        this.stocks.push(value);
        this.count = this.stocks.length - 1;
        this.curr_stock = this.stocks[this.count];
      }
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

<template>
<div id="stockpage">
    <b-container id="stock-canvas">
        <b-row>
            <b-col>
              <h1> {{ stocks[count] }} </h1>  
            </b-col>

        </b-row>

        <b-row>
            
            <b-col cols >
                <b-button class= "stockPageButton" v-on:click="previousStock">Previous</b-button>
            </b-col>
            
            <b-col cols>
                <b-button class= "stockPageButton" v-on:click="nextStock">Next</b-button>
               
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
        'stock3'],
      count: 0,
    };
  },
  methods: {
    nextStock() {
      if (this.count === this.stocks.length - 1) {
        this.count = 0;
      } else {
        this.count += 1;
      }
    },
    previousStock() {
      if (this.count === 0) {
        this.count = this.stocks.length - 1;
      } else {
        this.count -= 1;
      }
    },
  },
};
</script>

 
<style>
    .stockPageButton{
        background-color: #C7F0DB;
        color: #000000;
        
    }
  
</style>

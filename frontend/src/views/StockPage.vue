<template>
  <div class="stockpage">
      <b-container>
        <b-row>
          <b-col>
            <StockSearch/>
          </b-col>
          <b-col cols="7">
            <h1>{{title}}</h1>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <StockComponent/>
          </b-col>
          <b-col cols="7">
            <StockInfo/>
          </b-col>
        </b-row>
        <b-row>
          <b-col >
            <StockLog/>
          </b-col> 
          <b-col cols="7">
            
          </b-col>  
        </b-row>
      </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import StockComponent from '@/stocks/StockComponent.vue';
import StockSearch from '@/stocks/StockSearch.vue';
import StockLog from '@/stocks/StockLog.vue';
import StockInfo from '@/stocks/StockInfo.vue';

export default {
  name: 'StockPage',
  components: {
    StockComponent,
    StockSearch,
    StockLog,
    StockInfo,
  },
  data() {
    return {
      title: 'Interested in Stocks?',
    };
  },
  theme: {
    options: {
      customProperties: true,
    },
  },
};
</script>



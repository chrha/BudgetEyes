<template>
  <div class="stockpage">
    <b-container>
      <b-row>
        <b-col>
          <StockComponent/>
        </b-col>
        <b-col>
          <StockSearch/>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="7">
         
        </b-col>
        <b-col >
           <StockLog/>
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

export default {
  name: 'StockPage',
  components: {
    StockComponent,
    StockSearch,
    StockLog,
  },
};
</script>

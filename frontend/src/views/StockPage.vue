<template>
  <div class="stockpage">
    <navBar/>
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
import NavBar from '@/components/NavBar.vue';
import StockComponent from '@/stocks/StockComponent.vue';
import StockSearch from '@/stocks/StockSearch.vue';
import StockLog from '@/stocks/StockLog.vue';

export default {
  name: 'StockPage',
  components: {
    NavBar,
    StockComponent,
    StockSearch,
    StockLog,
  },
};
</script>

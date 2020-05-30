

<template>
  <div class="budgetpage">
    <div class="row">
      <div class="graph">
        <StockSearch/>
        <StockComponent/>
        <StockLog/>
        </div>
      <div class="inf">
          <StockInfo/>
      </div>
    </div>
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
    };
  },
  theme: {
    options: {
      customProperties: true,
    },
  },
};
</script>

<style scoped>
  .graph{

     float: left;
     margin: auto;
  }
  .inf{

     float: left;
     margin: auto;
  }

</style>

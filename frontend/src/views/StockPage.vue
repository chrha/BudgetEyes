

<template>
  <v-container fluid class="budgetpage">
    <v-row class="row">
      <v-col class="graph">
        <StockSearch/>
        <StockComponent/>
        <StockLog v-show="this.$store.state.username"/>
      </v-col>
      <v-col class="inf">
          <StockInfo/>
      </v-col>
    </v-row>
  </v-container>
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

<template>
    <div id='stock-info'>
      <v-card class="text-left"
      width="600px"
      color="#effcef">
        <v-card-title>
          Interested in Stocks?
        </v-card-title>
         <v-card-text class="stock-info">
           It is highly pleasant and efficient to be able to have an overview of
           stocks that you may be interested in, in a single place.
           This page provides such functionality where you can search for particular stocks,
           browse some of the more popular ones and log stocks you are interested in.
         </v-card-text>
     </v-card>
    </div>
</template>

<script>
export default {
  name: 'StockInfo',
  data() {
    return {
    };
  },
};
</script>

<style scoped >
  .text-left{
    text-align: left;
  }
  .font-regular{
    font-size: 30px;
  }
  .v-card-text{
    font-size: 1.3em
  }
</style>

<template>
    <div id='stock-info'>
      <div class="center">
        <v-card class="text-left"
        color="#effcef">
          <v-card-title class="justify-center" style="font-size: 2.0em">
            Interested in Stocks?
          </v-card-title>
           <v-card-text class="stock-info" style="font-size: 1.3em">
             It is highly pleasant and efficient to be able to have an overview of
             stocks that you may be interested in, in a single place.
             This page provides such functionality where you can search for particular stocks,
             and follow stocks you are interested in.
           </v-card-text>
       </v-card>
      </div>

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
.center {
  margin: auto;
  width: 100%;
  padding: 10px;
  margin-top:50px;
}
  .text-left{
    text-align: left;
  }
  .font-regular{
    font-size: 30px;
  }
</style>

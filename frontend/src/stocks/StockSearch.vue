<template>
<div id="stock-search">
    <b-container>
      <b-row>
        <b-col  >
             <v-text-field label="Enter stock name"></v-text-field>
        </b-col>
        <b-col>
           <v-btn id= "stockSearchButton" >Search</v-btn>
        </b-col>
      </b-row>
    </b-container>
</div>
</template>

<script>
export default {
  name: 'StockSearch',
};
</script>


<style scoped>
    #stockSearchButton{
      float: left;
      background-color: #C7F0DB;
      color: #000000;
    }
    
</style>

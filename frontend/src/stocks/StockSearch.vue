<template>
<div id="stock-search">
    <b-container>
      <b-row>
        <b-col >
             <input class=searchbar> 
             <b-button class= "stockPageButton">Search</b-button>
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
.stockPageButton{
    background-color: #C7F0DB;
    color: #000000;
    
}
.searchbar {
    background-color: white;
}

</style>

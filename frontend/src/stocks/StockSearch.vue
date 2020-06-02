<template>
<div class="center">
    <v-container class="cont">
      <v-row  class="ro">
        <v-col  cols="9" class="co">
          <v-autocomplete id="search-bar"
            full-width
            v-model="searchStock"
            :items="stockNameList"
            @keyup.enter="SearchStock(searchStock)"
            :search-input.sync="search"
            color="black"
            :filter="nameAndAbbrFilter"
            hide-no-data
            hide-selected
            cache-items
            item-text="name"
            item-value="abbr"
            label="Search"
            placeholder="Enter stock name"
            prepend-icon="mdi-database-search"
            return-object
          ></v-autocomplete>
        </v-col>
        <v-col class="bu">
              <v-btn id= "stockSearchButton" @click="SearchStock(searchStock)">Search</v-btn>
        </v-col>
      </v-row>
    </v-container>
</div>
</template>

<script>
import axiosInstance from '../ajax/client';

export default {
  name: 'StockSearch',
  data() {
    return {
      searchStock: '',
      search_res: '',
      stockNameList: [],
      search: null,
    };
  },
  mounted() {
    if (this.$store.getters.getStocks.length) {
      this.stockNameList = this.$store.getters.getStocks;
    } else {
      axiosInstance.get('stocks/get_abbr/')
        .then((response) => {
          const grid = response.data;
          this.$store.commit('setStocks', grid);
          this.stockNameList = grid;
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    }
  },
  methods: {
    SearchStock(searchStock) {
      // const sendData = { stocks: [searchStock.abbr] }; 
      this.$store.dispatch('requestStockData', { abbr: searchStock.abbr, period: 7 })
        .then(() => {
          this.search_res = this.$store.getters.getStockDataByAbbr({ abbr: searchStock.abbr, period: 'Weekly' });
          this.$root.$emit('msg_from_stocksearch', [searchStock.name, searchStock.abbr, this.search_res]);
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.$root.$emit('msg_from_stocksearch', [searchStock.name, searchStock.abbr, {}]);
        });

      /*
      axiosInstance.put('/stocks/query/', sendData)
        .then((response) => {
          this.search_res = response.data[searchStock.abbr];
          this.$root.$emit('msg_from_stocksearch', 
            [searchStock.name, searchStock.abbr, this.search_res]);
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
        */
    },
    nameAndAbbrFilter(item, queryText) {
      const name = item.name.toLowerCase();
      const abbr = item.abbr.toLowerCase();
      const searchText = queryText.toLowerCase();
      return searchText.length > 1 && (name.indexOf(searchText) > -1
        || abbr.indexOf(searchText) > -1);
    },
  },
};
</script>


<style scoped>
<<<<<<< HEAD
.stockPageButton{
    background-color: #C7F0DB;
    color: #000000;
    
}
.searchbar {
    background-color: white;
}
=======
  #search-bar{
    float: right;
  }
  .center {
    margin: auto;
    width: 100%;
    padding: 10px;
  }
  .bu{
    padding: 40px;
  }
  #stockSearchButton{
    background-color: #C7F0DB;
    color: #000000;
    position: absolute;
    left: 0;
  }
>>>>>>> development

</style>

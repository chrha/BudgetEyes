<template>
<div id="stock-search">
    <b-container>
      <b-row>
        <b-col  >
          <v-autocomplete
            v-model="searchStock"
            :items="stockNameList"
            @keyup.enter="SearchStock(searchStock)"
            :search-input.sync="search"
            color="black"
            :filter="filterFunc"
            hide-no-data
            hide-selected
            cache-items
            item-text="name"
            item-value="abbr"
            label="Search"
            placeholder="Enter stock name"
            prepend-icon="mdi-database-search"
          ></v-autocomplete>
        </b-col>
        <b-col>
           <v-btn id= "stockSearchButton" @click="SearchStock(searchStock)">Search</v-btn>
        </b-col>
      </b-row>
    </b-container>
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
    axiosInstance.get('stocks/get_abbr/', { headers: { Authorization: `Token ${this.$cookies.get('token')}` } })
      .then((response) => {
        const grid = response.data;
        this.$store.commit('setStocks', grid);
        this.stockNameList = grid;
      }).catch((error) => {
        console.log(error);
      });
  },
  methods: {
    SearchStock(searchStock) {
      const sendData = { stockname: searchStock };
      console.log(searchStock);
      axiosInstance.put('/stocks/searches/', sendData, { headers: { Authorization: `Token ${this.$cookies.get('token')}` } })
        .then((response) => {
          console.log('Resp:', response.data);
          this.search_res = response.data[searchStock];
          console.log(this.search_res);
          this.$root.$emit('msg_from_stocksearch', this.search_res);
        }).catch((error) => {
          console.log(error);
        });
    },
    filterFunc(item, queryText) {
      const textOne = item.name.toLowerCase();
      const textTwo = item.abbr.toLowerCase();
      const searchText = queryText.toLowerCase();

      return textOne.indexOf(searchText) > -1
        || textTwo.indexOf(searchText) > -1;
    },
  },
  computed: {
  },
};
</script>


<style scoped>
    #stockSearchButton{
      float: left;
      background-color: #C7F0DB;
      color: #000000;
    }
    
</style>

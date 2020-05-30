<template>
  <v-card class="deep-purple darken-1" max-width="450">
    <v-card-title class="headline"> 
      {{ stockName }} 
      <v-spacer> </v-spacer>
      <v-btn-toggle
      v-model="period"
      background-color="deep-purple accent-3"
      color="white"
      group
      mandatory
      @change="periodChange"
      >
      <v-btn value='1'> Daily </v-btn>
      <v-btn value='7'> Weekly </v-btn>
      <v-btn value='30'> Monthly </v-btn>
      </v-btn-toggle>
    </v-card-title>
    <v-progress-linear
      color="deep-purple accent-4"
      :active="loading"
      indeterminate
      rounded
      height="6"> 
    </v-progress-linear>
    <v-card-actions>
        <v-select
        v-model="model"
        :items="options"
        hint="Choose which types of prices to show"
        persistent-hint
        multiple
        :menu-props="{ openOnHover:true, openDelay:100, top:true, nudgeRight: 290}"
        solo
        dense
        small-chips
        deletable-chips
        color="white"
        item-color="black"
        background-color="deep-purple darken-1"
        @change="updateChartData()"
        >
        </v-select>
    </v-card-actions>
  <GChart
    type="LineChart"
    :data="chartData"
    :options="chartOptions"
    ref="graph"
    />
  <v-card-text v-show="dataNotFound" class="error"> This data is not available! </v-card-text>
  </v-card>
  
</template>

<script>

import axiosInstance from '../ajax/client';

export default {
  name: 'StockGraph',
  props: {
    stockData: {
      type: Object,
    },
    stockName: {
      type: String,
    },
    isDaily: {
      type: Boolean,
    },
  },
  watch: {
    stockData() {
      this.stock = this.stockData;
      this.period = '7';
      this.updateChartData();
    },
  },
  data() {
    return {
      stock: this.stockData,
      chartError: false,
      period: '7',
      dataNotFound: false,
      chartData: [
      ],
      loading: false,
      options: ['Close', 'Open', 'High', 'Low'],
      model: ['Close'],
      chartOptions: {
        backgroundColor: '#BBDEFB',
        width: 450,
        vAxis: {
          title: 'Price (USD)',
          gridlines: {
            color: 'grey',
          },
        },
      },
    };
  },
  methods: {
    updateChartData() {
      const values = Object.values(this.model);
      if (!values.length) {
        return;
      }
      this.chartData = [];
      const index = ['Date'];
      for (let i = 0; i < values.length; i += 1) {
        index.push(values[i]);
      }
      this.chartData.push(index);

      for (let i = 0; i < this.stock.Close.length; i += 1) {
        const tmparr = [];
        tmparr.push(this.stock.Dates[i]);
        for (let j = 0; j < this.model.length; j += 1) { 
          tmparr.push(this.stock[this.model[j]][i]);
        }
        this.chartData.push(tmparr);
      }
    },
    periodChange() {
      const period = Number(this.period);
      this.loading = true;
      axiosInstance.put('stocks/query/', { stocks: [this.stockName], period })
        .then((response) => {
          this.loading = false;
          this.stock = response.data[this.stockName];
          this.updateChartData();
          this.$refs.graph.$refs.chart.style.display = 'block';
          this.dataNotFound = false;
        }).catch(() => {
          this.$refs.graph.$refs.chart.style.display = 'none';
          this.dataNotFound = true;
          this.loading = false;
        }).finally(() => {
        });
    },  
  },
  mounted() {
    this.updateChartData();
  },
};
</script>


<style scoped>

</style>

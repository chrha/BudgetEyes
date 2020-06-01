<template>
  <v-card class="chart"
   color="deep-purple lighten-1">
    <v-card-title class="headline">
      {{ stockName }}
      <v-spacer> </v-spacer>
      <v-btn-toggle
      v-model="period"
      background-color="deep-purple lighten-2"
      color="black"
      group
      mandatory
      @change="periodChange"
      >
      <v-btn value='1' :loading="loadingDaily"> Daily </v-btn>
      <v-btn value='7' :loading="loadingWeekly"> Weekly </v-btn>
      <v-btn value='30' :loading="loadingMonthly"> Monthly </v-btn>
      </v-btn-toggle>
    </v-card-title>
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
        background-color="deep-purple lighten-2"
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
      loadingDaily: false,
      loadingWeekly: false,
      loadingMonthly: false,
      options: ['Close', 'Open', 'High', 'Low'],
      model: ['Close'],
      chartOptions: {
        backgroundColor: '#BBDEFB',
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
      if (period === 7) {
        this.loadingWeekly = true;
      } else if (period === 30) {
        this.loadingMonthly = true;
      } else {
        this.loadingDaily = true;
      }
      axiosInstance.put('stocks/query/', { stocks: [this.stockName], period })
        .then((response) => {
          this.stock = response.data[this.stockName];
          this.updateChartData();
          this.$refs.graph.$refs.chart.style.display = 'block';
          this.dataNotFound = false;
        }).catch(() => {
          this.$refs.graph.$refs.chart.style.display = 'none';
          this.dataNotFound = true;
        }).finally(() => {
          this.loadingMonthly = false;
          this.loadingWeekly = false;
          this.loadingDaily = false;
        });
    },
  },
  mounted() {
    this.updateChartData();
  },
};
</script>


<style scoped>
  .chart{
    width: 100%
  }
</style>

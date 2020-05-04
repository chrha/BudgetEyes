
<template>
  <div class="block">
    <div class="center">
      <h4 class="text-right"> <br>{{ intro }} </h4>
      <v-text-field
        label ="Salary">
      </v-text-field>
      <div  v-for="count in count" :key=count>
        <v-text-field
        label="Expense Nr.">
          <v-icon slot="append" color="red" v-on:click="incramentCounter">mdi-plus</v-icon>
        </v-text-field>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'BudgetCalc',
  data() {
    return {
      count: 2,
      intro: 'Enter monthly income and expenses to find out your budget!',
    };
  },
  methods: {
    incramentCounter() {
      this.count += 1;
    },
  },
};

</script>
 <style scoped>

.center {
  margin: auto;
  width: 100%;
  padding: 10px;
}

</style>

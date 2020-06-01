<template>
  <v-container class="budgetpage">
    <v-row class="row">
      <v-col class="calc">
        <BudgetCalc/>
      </v-col>
      <v-col class="inf">
        <BudgetInfo/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src
import BudgetCalc from '@/budget/BudgetCalc.vue';
import BudgetInfo from '@/budget/BudgetInfo.vue';

export default {
  name: 'BudgetPage',
  components: {
    BudgetCalc,
    BudgetInfo,
  },
};

</script>
 <style scoped>

 .calc {
  float: left;
  margin: auto;
}
.inf {
  background-color: transparent;
  float: left;
  width: 100%;
  margin-right: auto;}

</style>

<template>
  <div class="budgetpage">
    <div class="row">
      <div class="calc">
        <BudgetCalc/>
        </div>
      <div class="inf">
        <BudgetInfo/>
      </div>
    </div>
  </div>
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
  margin-right: auto;}

</style>

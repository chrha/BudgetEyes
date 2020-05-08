<template>
  <div class="budgetpage">
    <div class="row">
      <div class="column">
        <BudgetCalc/>
        </div>
      <div class="column">
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

 .column {
  float: left;
  margin: auto;
}
.center {
  margin: auto;
  width: 50%;
  border: 3px solid green;
  padding: 10px;
}

</style>

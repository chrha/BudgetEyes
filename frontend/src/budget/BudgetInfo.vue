
<template>
  <div class="column">
    <v-card class="wise-words"
      width="600px"
      color="#effcef">
      <v-card-text>
        Budgeting is important
        because it helps you accurately plan,
        control and track how much money you spend, save, give and invest.
        Additionally, budgeting helps you stay financially organized,
        prepare for emergencies,
        steer clear of debt, and maintain focus on your long-term goals
      </v-card-text>

      <v-card-text>
        This calculator uses the 50/30/20 budgeting method which
        divides your monthly expenses into needs , wants and savings.
        50% of your income should be allocated towards needs, 30% to wants
        and 20% towards savings.
      </v-card-text>
    </v-card>
  </div>
</template>

<script>

export default {
  name: 'BudgetInfo',
  data() {
    return {
    };
  },
};

</script>
 <style scoped>

.center {
  width: 100%;
  padding: 10px;
  overflow: hidden;
  text-overflow:ellipsis;
}
.wise-words{
  font-size: 18px;
  text-align: left;
  margin-top:50px;
}

.column{
  background-color: transparent;
}

</style>

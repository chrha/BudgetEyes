
<template>
  <div class="center">
    <v-card class="wise-words"
      color="#effcef">
      <v-card-title class="justify-center" style="font-size: 2.0em">
        Don't neglect your budget!
      </v-card-title>
      <v-card-text style="font-size: 1.3em">
        Budgeting is important
        because it helps you accurately plan,
        control and track how much money you spend, save, give and invest.
        Additionally, budgeting helps you stay financially organized,
        prepare for emergencies,
        steer clear of debt, and maintain focus on your long-term goals
      </v-card-text>

      <v-card-text style="font-size: 1.3em">
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
  margin: auto;
  width: 100%;
  padding: 10px;
  overflow: hidden;
  text-overflow:ellipsis;
}
.wise-words{
  text-align: left;
  margin-top:50px;
}

</style>

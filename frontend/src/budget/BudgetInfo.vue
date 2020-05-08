
<template>
  <div class="block">
    <div class="center">
      <div class = info>
        <p> <br>Budgeting is important because it helps you accurately plan,<br>
            control and track how much money you spend, save, give and invest.<br>
            Additionally, budgeting helps you stay financially organized,<br>
            prepare for emergencies,<br>
            steer clear of debt, and maintain focus on your long-term goals</p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'BudgetInfo',
  data() {
    return {
      count: 4,
      infoList: ['budgeting is important because it helps you accurately plan,',
        'control and track how much money you spend, save, give and invest.',
        'Additionally, budgeting helps you stay financially organized, prepare for emergencies,',
        'steer clear of debt, and maintain focus on your long-term goals.'],
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
}
.info{
  font-size: 22px;
  color: black;
  text-align: left;

}

</style>

<template>
  <v-container>
    <div v-if="this.$store.state.username">
      <span> Hey {{ $store.state.username }}! You are following these stocks: </span>
    </div>
    <div v-else-if="user">
      <span> Bye {{ user }}, do come back again! </span>
    </div>
    <div v-else>
      <span> Welcome to BudgetEyes </span>
    </div>
  </v-container>
</template>

<script>
export default {
  name: 'HomePage',
  props: {
    previous: {
      type: String,
    },
  },
  data() {
    return {
      user: this.previous,
    };
  },
};
</script>

<style>

</style>

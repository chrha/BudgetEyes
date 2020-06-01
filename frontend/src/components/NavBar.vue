
<template>
  <div id="navbar-app">
    <div>
      <b-navbar class = "navbar">
          <b-navbar-brand href="#/">
              <img class="logo" src="https://upload.wikimedia.org/wikipedia/commons/f/f0/Eye-Brown.svg" alt="BE" style="width:40px;height:40px;">
          </b-navbar-brand>

          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

          <b-collapse class="nav-collapse" is-nav>
              <b-navbar-nav class="navbar-nav">
                    <b-nav-item class="navbar-item-custom" href="#/budgetpage">Budget</b-nav-item>
                  <b-nav-item class="navbar-item-custom" href="#/stockpage">Stocks</b-nav-item>
              </b-navbar-nav>

              <!-- Right aligned nav items -->
              <b-navbar-nav class="ml-auto">
                <b-nav-item-dropdown right v-if="this.$store.state.username">
                    <!-- Using 'button-content' slot -->
                    <template v-slot:button-content>
                        <em> {{ $store.state.username }} </em>
                    </template>
                    <b-dropdown-item @click="routeProfile"> Profile </b-dropdown-item>
                    <b-dropdown-item @click="logOut"> Sign Out </b-dropdown-item>
                </b-nav-item-dropdown>
                <b-navbar-nav v-else class="navbar-nav">
                  <b-nav-item class="navbar-item-custom" @click="routeLogin">Log in</b-nav-item>
                  <b-nav-item class="navbar-item-custom" @click="routeRegister">Sign up</b-nav-item>
                </b-navbar-nav>
              </b-navbar-nav>
          </b-collapse>
      </b-navbar>
    </div>
  </div>
</template>



<script>
export default {
  name: 'navBar',
  methods: {
    routeLogin() {
      this.$router.push({ name: 'Login' }).catch(() => {});
    },
    routeRegister() {
      this.$router.push({ name: 'Register' }).catch(() => {});
    },
    routeProfile() {
      this.$router.push({ name: 'ProfilePage' }).catch(() => {});
    },
    logOut() {
      this.$cookies.remove('token');
      this.$cookies.remove('username');
      const tmpuser = this.$store.state.username;
      this.$store.commit('setUsername', '');
      this.$router.push({ name: 'Home', params: { previous: tmpuser } }).catch((err) => { console.log(err); });
    },
  },
};
</script>


 <style>
.navbar .nav-collapse .navbar-nav .navbar-item-custom{
    color: #b30b0b;
}
.navbar-item-custom{
  font-size: 16px;
}
.navbar{
background-color: #6c7b95;
height: 40px;
}
.logo{
    size: 20px;
}

</style>

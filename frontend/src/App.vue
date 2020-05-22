<template>
  <div id="app">
    <Nav/>
    <v-app id="v-app">
    <router-view/>
    </v-app>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue';


export default {
  components: {
    Nav: NavBar,
  },
};
</script>

<style>

html {
  height: 100%;
}

#v-app {
  background: linear-gradient(to bottom right, #effcef, #ccedd2, #94d3ac, #655c56);
  min-height: 100%;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

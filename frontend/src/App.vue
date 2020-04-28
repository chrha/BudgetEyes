<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>

html {
  height: 100%;
}

body {
  background: linear-gradient(to bottom, #effcef, #ccedd2, #94d3ac, #655c56);
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

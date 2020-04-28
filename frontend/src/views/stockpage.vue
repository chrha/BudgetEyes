<template>
  <div class="stockpage">
    <navBar/>
  </div>
</template>
<script>
// @ is an alias to /src
import navBar from '@/components/navbar.vue';


export default {
  name: 'stockPage',
  components: {
    navBar,
  },
};
</script>

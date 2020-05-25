<template>
  <div class="main">

    <p v-if="this.message"> {{ message }} </p>
    <v-card class="mx-auto deep-purple lighten-4" max-width="500">
      <h2 class="header mt-5"> Login </h2>
        <v-form ref="form" @submit.prevent="Login">
          <v-text-field
          v-model="form.username"
          label="Username"
          prepend-icon="mdi-account"
          :rules="nameRules"
          @keyup.enter="Login"
          autocomple="username"
          >
          </v-text-field>
          <v-text-field
          v-model="form.password"
          label="Password"
          prepend-icon="mdi-lock"
          required
          :type="'password'"
          :rules="passwordRules"
          @keyup.enter="Login"
          autocomplete="password"
          > </v-text-field>
          <v-btn 
          class="mt-4 gray darken-3" width="400" @click="Login"> Sign in </v-btn>
        </v-form>
        <v-card-text>
            <router-link to="/register" style="color:black"> 
              Not registred? Sign up here 
            </router-link>
        </v-card-text>
      </v-card>
    </div>
</template> 

<script>
import axiosInstance from '../ajax/client';

export default {
  name: 'LoginPage',
  props: ['msg'],
  data() {
    return {
      message: this.msg,
      form: {
        username: '',
        password: '',
      },
      nameRules: [(v) => !!v || 'Username is required'],
      passwordRules: [(v) => !!v || 'Password is required'],
    };
  },
  methods: {
    Login() {
      if (this.$refs.form.validate()) {
        axiosInstance.put('auth/login/', {
          username: this.form.username,
          password: this.form.password,
        }).then((response) => {
          const token = response.headers.authorization;
          this.$cookies.set('token', token);
          this.$cookies.set('username', this.form.username);
          this.$store.commit('setUsername', this.form.username);
          this.$router.push({ name: 'Home' });
        }).catch((error) => {
          // eslint-disable-next-line 
          alert(error);
        });
      }
    },

    Reset() {
      this.form.username = '';
      this.form.password = '';
    },
  },
};
</script>


<style scoped>

</style>

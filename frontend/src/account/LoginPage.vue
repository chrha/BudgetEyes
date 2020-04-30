<template>
  <div class="main">
    <NavBar></NavBar>

    <p v-if="this.message"> {{ message }} </p>
    <h2 class="header mt-5"> Login </h2>
      <b-form id="loginform" @submit.prevent="Login" @reset="Reset">
        <b-form-input
          id="username-input"
          label="Username:"
          v-model="form.username"
          required
          placeholder="Enter username"
          autocomplete="username"
        >
        </b-form-input>
        <b-form-input
          id="password-input"
          label="Password:"
          v-model="form.password"
          type="password"
          required
          placeholder="Enter password"
          autocomplete="current-password"
        >
        </b-form-input>

        <b-button id="submit-b" class="mt-1" type="submit" variant="primary">Submit</b-button>
        <b-button id="reset-b" class="mt-1" type="reset" variant="danger">Reset</b-button>
        <div class="link-div">
          <router-link class="signup-link" to="/register">
          Not registred? Sign up here
          </router-link>
        </div>
      </b-form>
  </div>
</template>

<script>
import Nav from '@/components/navbar.vue';
import axiosInstance from '../ajax/client';

export default {
  name: 'LoginPage',
  props: ['msg'],
  components: {
    NavBar: Nav,
  },
  data() {
    return {
      message: this.msg,
      form: {
        username: '',
        password: '',
      },
    };
  },
  methods: {
    Login() {
      axiosInstance.put('auth/login/', {
        username: this.form.username,
        password: this.form.password,
      }).then((response) => {
        const token = response.headers.authorization;
        this.$store.commit('setToken', token);
        this.$store.commit('setUsername', this.form.username);
      }).catch((error) => {
        // eslint-disable-next-line 
        alert(error);
      });
    },

    Reset() {
      this.form.username = '';
      this.form.password = '';
    },
  },
};
</script>


<style scoped>

#loginform {
    position: relative;
    padding-left: 30%;
    padding-right: 30%;
}

.link-div {
  margin-top : 1.5%;
}

.signup-link {
  font-size: 20px;
  color: black;
  padding-left: 5%;
  float : left;
}

#submit-b {
  float : left;
}

#reset-b {
  float : left;
}
</style>

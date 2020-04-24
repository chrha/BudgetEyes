<template>
  <div class="main">
    <h2 class="header"> Login </h2>
      <b-form id="loginform" @submit.prevent="Login" @reset="Reset">
        <b-form-input
          id="username-input"
          label="Username:"
          v-model="form.username"
          required
          placeholder="Enter username"
        >
        </b-form-input>
        <b-form-input
          id="password-input"
          label="Password:"
          v-model="form.password"
          type="password"
          required
          placeholder="Enter password"
        >
        </b-form-input>

        <b-button id="submit-b" class="mt-1" type="submit" variant="primary">Submit</b-button>
        <b-button id="reset-b" class="mt-1" type="reset" variant="danger">Reset</b-button>
        <div class="link-div">
          <a class="signup-link" href="#"> Not registred? Sign up here </a>
        </div>
      </b-form>
  </div>
</template>

<script>
import server from '../ajax/client';

export default {
  name: 'LoginPage',
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
    };
  },
  methods: {
    Login() {
      server.post('/ex/', {
        username: this.username,
        password: this.password,
      }).then((response) => {
        alert(response);
      }).catch((error) => {
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

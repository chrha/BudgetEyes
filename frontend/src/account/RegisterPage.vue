<template>
  <div>
  <h2 class="register"> Create account </h2>
  <b-form @submit.prevent="Register">
    <b-form-group class=reg-grp> 
      <b-form-input
        id="fname"
        label="Firstname"
        v-model="form.first_name"
        required
        placeholder="Enter your firstname"   
      >
      </b-form-input>
      <b-form-input
        id="lname"
        label="Lastname"
        v-model="form.last_name"
        required
        placeholder="Enter your lastname" 
      >
      </b-form-input>
      <b-form-input
        id="uname"
        label="Username"
        v-model="form.username"
        required
        placeholder="Enter your username"
        autocomplete="username"
      >
      </b-form-input>
      <b-form-input
        id="email"
        label="Email"
        v-model="form.email"
        type="email"
        required
        placeholder="Enter your email address"   
      >
      </b-form-input>
      <b-form-input
        id="pword"
        label="Password"
        v-model="form.password"
        type="password"
        required
        placeholder="Enter your password"
        autocomplete="new-password"
      >
      </b-form-input>
      <b-form-input
        id="re-pword"
        label="Re-enter Password"
        v-model="form.rePassword"
        type="password"
        required
        placeholder="Enter your password again"
        autocomplete="new-password"
      >
      </b-form-input>
      <b-button class=submitbutton type="submit"> Register </b-button>
    </b-form-group>
  </b-form>
    <p v-if="errors.length === 1">
        <ul>
          <p class=error-item> {{errors[0]}} </p>
        </ul>
    </p>
    <p v-else-if="errors.length">
      <b>Please correct the following errors:</b>
      <ul>
        <li v-for="error in errors" :key="error"><strong> {{ error }} </strong></li>
      </ul>
    </p>
  </div>
</template>

<script>

import axiosInstance from '../ajax/client';

export default {
  name: 'Register',
  data() {
    return {
      errors: [],
      form: {
        first_name: '',
        last_name: '',
        username: '',
        email: '',
        password: '',
        rePassword: '',
      },
    };
  },
  methods: {
    Register() {
      if (this.form.password !== this.form.rePassword) {
        if (!this.errors.length) this.errors.push('Passwords must match');
      } else {
        axiosInstance.put('auth/register/', this.form).then(() => { 
          this.$router.push({ name: 'Login', params: { msg: 'User created!' } });
        }).catch((response) => {
          // eslint-disable-next-line 
          console.log(response);
        });
      }
    },
  },
};
</script>


<style scoped>

.register {
  margin-top: 4%
}

.reg-grp {
  margin-left: 30%;
  margin-right: 30%;
}

.submitbutton {
  margin-top: 1%;
  float: left ;
}
.error-item {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif ;
  font-size: 30px;
}

</style>

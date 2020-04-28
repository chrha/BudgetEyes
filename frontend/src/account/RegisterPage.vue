<template>
  <div>
  <NavBar></NavBar>
  <h2 class="register"> Create account </h2>
  <b-form @submit.prevent="Register">
    <b-form-group class=reg-grp> 
      <b-form-input
        id="fname"
        label="Firstname"
        v-model="form.firstName"
        required
        placeholder="Enter your firstname"   
      >
      </b-form-input>
      <b-form-input
        id="lname"
        label="Lastname"
        v-model="form.lastName"
        required
        placeholder="Enter your lastname" 
      >
      </b-form-input>
      <b-form-input
        id="uname"
        label="Username"
        v-model="form.userName"
        required
        placeholder="Enter your username"   
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
      >
      </b-form-input>
      <b-form-input
        id="re-pword"
        label="Re-enter Password"
        v-model="form.rePassword"
        type="password"
        required
        placeholder="Enter your password again"   
      >
      </b-form-input>
      <b-button class=submitbutton type="submit"> Register </b-button>
    </b-form-group>
  </b-form>
    <p v-if="errors.length === 1">
      <b>Please correct the following error:</b>
        <ul>
          <li> {{errors[0]}} </li>
        </ul>
    </p>
    <p v-else-if="errors.length !== 0">
      <b>Please correct the following errors:</b>
      <ul>
        <li v-for="error in errors" :key="error">{{ error }}</li>
      </ul>
    </p>
  </div>
</template>

<script>

import Nav from '@/components/navbar.vue';
// import server from '@/ajax/client';

export default {
  name: 'Register',
  components: {
    NavBar: Nav,
  },
  data() {
    return {
      errors: [],
      form: {
        firstName: '',
        lastName: '',
        userName: '',
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
        this.errors.pop();
        // server.post('/example', this.form);
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


</style>

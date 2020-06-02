<template>
  <div>
  <h2 class="register"> Create account </h2>
  <v-card class="mx-auto deep-purple lighten-4" max-width="500">
    <v-form ref="form">
      <v-text-field
      v-model="form.first_name"
      label="First name (optional)"
      :filled="true"
      :clearable="true"
      @keyup.enter="Register"
      >
      </v-text-field>
      <v-text-field
      v-model="form.last_name"
      label="Last name (optional)"
      :clearable="true"
      :filled="true"
      @keyup.enter="Register"
      >
      </v-text-field>
      <v-text-field
      v-model="form.username"
      label="Username"
      :clearable="true"
      :filled="true"
      :rules="usernameRules"
      @keyup.enter="Register"
      @input="usernameAvailable = true"
      >
      </v-text-field>
      <v-text-field
      v-model="form.email"
      label="Email"
      :filled="true"
      :clearable="true"
      :rules="emailRules"
      @keyup.enter="Register"
      >
      </v-text-field>
      <v-text-field
      v-model="form.password"
      label="Enter password"
      type="password"
      :filled="true"
      :clearable="true"
      :rules="passwordRules"
      @keyup.enter="Register"
      >
      </v-text-field>
      <v-text-field
      v-model="form.rePassword"
      label="Enter password again"
      type="password"
      :filled="true"
      :clearable="true"
      :rules="rePasswordRules"
      @keyup.enter="Register"
      >
      </v-text-field>
      <v-btn class="mt-2 gray darken-3" width="400" @click="Register"> Register </v-btn>
    </v-form>
  </v-card>
  </div>
</template>

<script>

import axiosInstance from '../ajax/client';

export default {
  name: 'Register',
  data() {
    return {
      form: {
        first_name: '',
        last_name: '',
        username: '',
        email: '',
        password: '',
        rePassword: '',
      },
      usernameAvailable: true,
      usernameRules: [
        (v) => !!v || 'Username is required',
        () => !!this.usernameAvailable || 'That username is already taken!',
      ],
      emailRules: [
        (v) => !!v || 'Email is required',
        (v) => !v || /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid',
      ],
      passwordRules: [
        (v) => !!v || 'Password is required',
        (v) => !v || /^(?=.*\d).{8,16}$/.test(v) || 'Password must be between 8 and 16 characters long and contain at least one digit',
      ],
      rePasswordRules: [
        (v) => !!v || 'You must enter password twice',
        () => (this.form.rePassword === this.form.password) || 'Passwords must match', 
        (v) => !v || /^(?=.*\d).{8,16}$/.test(v) || 'Password must be between 8 and 16 characters long and contain at least one digit',
      ],
    };
  },
  methods: {
    Register() {
      if (this.$refs.form.validate()) {
        axiosInstance.put('auth/register/', this.form).then(() => { 
          this.$router.push({ name: 'Login', params: { msg: 'User created!' } });
        }).catch((error) => {
          if (error.response.status === 400) {
            this.usernameAvailable = false;
            this.$refs.form.validate();
          }
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

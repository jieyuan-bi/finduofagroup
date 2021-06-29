<template>
  <div class="container" style="margin-top:20px">
    <div
      style="margin-bottom:20px"
      class="align-items-center text-white bg-success border-0"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
      data-delay="2000"
      v-if="message"
    >
      <div class="d-flex">
        <div class="toast-body">成功注册，请登录</div>
        <button
          type="button"
          class="btn-close btn-close-white me-2 m-auto"
          data-bs-dismiss="toast"
          aria-label="Close"
        ></button>
      </div>
    </div>

    <form @submit.prevent="submitLogin">
      <div class="mb-3">
        <label for="signup_account" class="form-label">账号 Account</label>
        <input type="text" class="form-control" id="signup_account" v-model="account" />
      </div>
      <div class="mb-3">
        <label for="inputPassword5" class="form-label">密码 Password</label>
        <input type="password" id="signup_password" class="form-control" v-model="password" />
      </div>
      <div>
        <p>
          没有账号？
          <router-link :to="name='Signup'">点此</router-link>注册.
        </p>
        <p>
          No account? Click
          <router-link :to="name='Signup'">here</router-link>to signup.
        </p>
      </div>
      <div class="alert alert-danger" role="alert" v-if="errors.length">
          <p v-for="error in errors" :key="error">{{error}}</p>
        </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>


<script>
// @ is an alias to /src
import axios from "axios";

export default {
  name: "Login",
  components: {},
  data() {
    return {
      message: false,
      account: "",
      password: "",
      errors: [],

    };
  },
  methods: {
    checkMessage() {
      this.message = this.$route.params.message;
    },
    submitLogin() {
      this.errors = [];
      if (this.account == "") {
        this.errors.push("请输入用户名");
      }
      if (this.password == "") {
        this.errors.push("请输入密码");
      }
      if (!this.errors.length) {
        axios
          .post("/api/users/login", {
            account: this.account,
            password: this.password,
          })
          .then((response) => {
            console.log("response:" + response.data.success);
            if (response.data.success) {
              //change token to correspond value
              this.$store.commit({
                type:'login',
                role: response.data.role,
                account: this.account
              })
                // console.log('changed role to user',this.$store.state.token)
              
              
              this.$router.push({ name: "Home" ,params: { login: true }});
            }else{
              this.errors.push("账号或密码错误，请重试");
            }
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
  mounted() {
    this.checkMessage();
  },
};
</script>

<style rel="stylesheet/scss" lang="scss">
</style>
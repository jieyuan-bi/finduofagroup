<template>
    <div class="container" style="margin-top:20px">
      <form @submit.prevent="submitSignup" >
        <div class="mb-3">
          <label for="signup_name" class="form-label">* 姓名 Name</label>
          <input
            type="text"
            class="form-control"
            id="signup_name"
            placeholder="请尽量使用常用名"
            v-model="name"
          />
        </div>
        <div class="mb-3">
          <label for="signup_gender" class="form-label">* 性别 Gender</label>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="signup_gender" id="male" />
            <label class="form-check-label" for="flexRadioDefault1">男 Male</label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="signup_gender" id="female" />
            <label class="form-check-label" for="flexRadioDefault2">女 Female</label>
          </div>
        </div>
        <div class="mb-3">
          <label for="signup_email" class="form-label">邮箱 Email address</label>
          <input
            placeholder="请尽量使用主要邮箱"
            type="email"
            class="form-control"
            id="signup_email"
            aria-describedby="emailHelpBlock"
            v-model="email"
          />
          <div
            id="emailHelpBlock"
            class="form-text"
            style="display:"
          >Your email must be 8-20 characters long.</div>
        </div>
        <div class="mb-3">
          <label for="signup_phone" class="form-label">手机 Phone</label>
          <input
            placeholder="请输入正确号码"
            type="tel"
            class="form-control"
            id="signup_phone"
            aria-describedby="phoneHelpBlock"
            v-model="phone"
          />
          <div
            id="phoneHelpBlock"
            class="form-text"
            style="display:"
          >Your phone must be 8-20 characters long.</div>
        </div>
        <div class="mb-3">
          <label for="inputPassword1" class="form-label">* 密码 Password</label>
          <input
            type="password"
            id="inputPassword1"
            class="form-control"
            aria-describedby="passwordHelpBlock"
            v-model="password"
          />
          <div
            id="passwordHelpBlock"
            class="form-text"
            style="display:"
          >Your password must be 8-20 characters long.</div>
        </div>
        <div class="mb-3">
          <label for="inputPassword2" class="form-label">* 密码验证 Password Verification</label>
          <input
            type="password"
            id="inputPassword2"
            class="form-control"
            v-model="password2"
          />
        </div>
        <div class="mb-3">
          <label for="signup_onecard" class="form-label">Onecard</label>
          <input
            class="form-control"
            type="file"
            id="signup_onecard"
            aria-describedby="onecardHelpBlock"
          />
          <div
            id="onecardHelpBlock"
            class="form-text"
            style="display:"
          >为防止作业代写等恶意群体，请尽早上传onecard，验证通过后可使用网站全部功能</div>
        </div>
        <div class="mb-3">
          <label for="signup_department" class="form-label">学院 Department</label>
          <select
            v-model="signup_department"
            class="form-select"
            aria-label="Default select example"
          >
            <option selected>Open this select menu</option>
            <option v-for="c in catalogue" :key="c[1]" :value="c[1]">{{c[0]}}</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="signup_major" class="form-label">主修 Major</label>
          <select class="form-select" aria-label="Default select example" v-model="signup_major">
            <option selected>Open this select menu</option>
            <option v-for="s in subject[signup_department]" :key="s[1]" :value="s[1]">{{s[0]}}</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="signup_wechat" class="form-label">微信ID Wechat</label>
          <input class="form-control" type="text" id="signup_wechat" v-model="wechat" />
        </div>
        <div class="alert alert-danger" role="alert" v-if="errors.length">
          <p v-for="error in errors" :key="error">{{error}}</p>
        </div>
        <button class="btn btn-primary" style="margin-top:20px">Submit</button>
      </form>
    </div>
</template>


<script>
// @ is an alias to /src
import axios from "axios";

export default {
  name: "Signup",
  data() {
    return {
      name: "",
      email: "",
      phone: "",
      password: "",
      password2: "",
      wechat: "",
      property: "value",
      subject: {},
      catalogue: [],
      errors: [],
      signup_department: "",
      signup_major: "",
      gender: "",
    };
  },
  components: {},
  computed: {
    getGender() {
      if (document.getElementById("male").checked) {
        this.gender = "male";
      } else {
        this.gender = "female";
      }
    },
  },
  methods: {
    submitSignup() {
      this.getGender;
      //handle all possible errors
      this.errors = []
      if (this.name==''){
        this.errors.push('请输入用户名')
      }
      if (this.password==''){
        this.errors.push('请输入密码')
      }
      if (this.password!==this.password2){
        this.errors.push('密码不匹配')
      }
      if (!this.errors.length){
        var form_data = new FormData();
        var onecard = document.getElementById("signup_onecard").files[0];
        form_data.append('name', this.name);
        form_data.append('email', this.email);
        form_data.append('phone', this.phone);
        form_data.append('password', this.password);
        form_data.append('wechat', this.wechat);
        form_data.append('major', this.signup_major);
        form_data.append('gender', this.gender);
        form_data.append('onecard', onecard, onecard.name);
    //     var data={}
    //     for (var key of form_data.entries()) {
    //     data[key[0]]=key[1];
    // }
    // console.log(data)
      axios
        .post("/api/users/signup", form_data,{
    headers: {
        'Content-Type': 'multipart/form-data'
    }
  })
        //handle the result and try to create a new user
        .then((response) => {
          console.log("response:" + response.data.success);
          if (response.data.success == '-1'){
            this.errors.push('用户名已存在')
          }else if(response.data.success == '0'){
            this.errors.push('。。。可能出bug了，请记录具体过程并联系我们')
          }else if
             (response.data.success == "1") {
              this.$router.push({ name: "Login" , params: { message: true }});
              // console.log('account created')
            }
          
        })
        .catch((error) => {
          console.log(error);
        });
      }
    },
    createNav() {
      axios
        .get("/api/courses/course")
        .then((response) => {
          this.catalogue = response.data.catalogue;
          this.subject = response.data.subject;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    // console.log("mounted");
    this.createNav();
  },
};
</script>

<style rel="stylesheet/scss" lang="scss">
</style>
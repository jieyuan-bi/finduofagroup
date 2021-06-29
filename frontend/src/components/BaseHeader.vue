<template>
  <!-- <el-menu
    default-active="/home/"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b"
    :router="true"
  >
    <el-menu-item index="/home/" >Find U of A Group</el-menu-item>
    <el-submenu index="/group"  title="我加入的小组">
      <template #title><i class="fas fa-users"></i></template>
      <el-menu-item index="2-1">选项1</el-menu-item>
      <el-menu-item index="2-2">选项2</el-menu-item>
      <el-menu-item index="2-3">选项3</el-menu-item>
      <el-submenu index="2-4">
        <template #title>选项4</template>
        <el-menu-item index="2-4-1">选项1</el-menu-item>
        <el-menu-item index="2-4-2">选项2</el-menu-item>
        <el-menu-item index="2-4-3">选项3</el-menu-item>
      </el-submenu>
    </el-submenu>
    <el-menu-item index="/message" title="消息中心"><i class="fas fa-inbox"></i></el-menu-item>
    <el-menu-item index="/user" title="个人中心">
      <i class="fas fa-user"></i>
    </el-menu-item>
  </el-menu> -->
  <nav class="navbar navbar-expand-lg navbar-light bg-dark ">
  <div class="container-fluid">
    <router-link class="navbar-brand navbar-light-active-color" to='/home'>Find U of A Group</router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation" @click.stop="toggleNavbar()">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent" :class="{ 'show': show }">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <router-link class="nav-link active" aria-current="page" to='/Login'><i class="fas fa-inbox"></i>消息中心</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link active" aria-current="page" to='/Signup'><i class="fas fa-user"></i>个人中心</router-link>
        </li>
        <li class="nav-item" v-if="this.$store.state.token==2">
          <router-link class="nav-link active" aria-current="page" to='/Manage'><i class="fas fa-tasks"></i>管理</router-link>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
      </ul>
      <button type="button" class="btn btn-success d-flex" v-if="token==-1" @click="userLogin">登录/注册</button>
      <button type="button" class="btn btn-light d-flex" v-else @click="userLogout">退出</button>
    </div>
  </div>
</nav>
</template>

<script>
export default {
  data() {
    return {
      token: this.$store.state.token,
      show: false,

    };
  },
  methods: {
    userLogin(){
      this.$router.push({name:"Login"})
    },
    userLogout(){
      this.$store.commit('logout');
      window.location.reload();
    },
    toggleNavbar() {
      this.show = !this.show
    }
    // setToken(){
    //   console.log('param:login is ',this.$route.params.login)
    //   if(this.$route.params.login){
    //     window.location.reload();
    //   }
      // console.log(this.$store.state.token)
    // }
    // handleSelect(key, keyPath) {
    //   console.log(key, keyPath);
    // },
  },
  // mounted(){
  //   this.setToken();
  // },
  // watch:{
  //   token: function (newToken, oldToken) {
  //     window.location.reload();
  //   }
  // }
};
</script>

<style>
  .nav-link {
    color: rgb(211, 211, 211)!important;
  }

  .navbar-brand {
    color: rgb(211, 211, 211)!important;
  }
  
  .nav-item>a:hover {
    color: #646464!important;
  }
  
  .navbar-brand>a:hover {
    color: #646464!important;
  }
  
  .router-link-exact-active{
    color: rgb(177, 255, 140)!important;
  }
</style>
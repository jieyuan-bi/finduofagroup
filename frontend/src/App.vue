<template>
  <div>
    <el-container>
      <el-header height="10%">
        <el-affix id="header-affix">
        <base-header />
        </el-affix>
      </el-header>
      <el-main>
        <router-view />
      </el-main>
      <el-footer height="10%">Copyright (c) 2021</el-footer>
    </el-container>
  </div>
</template>



<script>
import Home from "@/views/Home.vue";
import BaseHeader from "./components/BaseHeader.vue";

export default {
  components: {
    Home,
    BaseHeader,
  },
  data() {
    return {};
  },
  mounted(){
    // this.$router.push('/home/')
  }
};
</script>


<style rel="stylesheet/scss" lang="scss">
// @import '../node_modules/bulma'

html,
body,
#app,
.el-container {
  padding: 0px;
  margin: 0px;
  height: 100%;
}

header.el-header {
  background-color: rgb(193, 251, 255);
  padding: 0px;
}

main.el-main {
  background-color: white;
  padding: 0px;
}

footer.el-footer {
  background-color: white;
  padding: 0px;
  text-align: center;
}
</style>

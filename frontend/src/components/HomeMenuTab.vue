<template>
  <div class="expand-container">
    <el-affix title="展开" id="drawer-affix" target=".expand-container" position="bottom">
      <el-button class="expand_menu" @click="drawer = true" type="text">
        <i class="el-icon-s-unfold"></i>
      </el-button>
    </el-affix>
    <el-drawer
      title="classes title"
      v-model="drawer"
      :with-header="false"
      :size="widthPercentage"
      :direction="direction"
    >
      <el-affix class="search_box" id="search-affix">
        <el-form :inline="true" class="demo-form-inline">
          <el-form-item label>
            <el-input v-model="formMsg" placeholder="课程名称" @keydown.enter.prevent="onSubmit"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">搜索</el-button>
          </el-form-item>
        </el-form>
      </el-affix>
      <div>
        <el-menu
          :default-active="$route.path"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
          background-color="#545c64"
          text-color="#fff"
          :router="true"
        >
          <el-submenu v-for="c in catalogue" :key="c[1]" :index="c[1]">
            <template #title>
              <span>{{c[0]}}</span>
            </template>
            <el-menu-item v-for="s in subject[c[1]]" :key="s[1]" :index="s[1]">{{s[0]}}</el-menu-item>
          </el-submenu>
        </el-menu>
      </div>
    </el-drawer>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      search_query: "",
      drawer: false,
      direction: "ltr",
      isCollapse: true,
      catalogue: [],
      subject: {},
      class: {},
      formMsg: "",
      //get the width of screen
      windowWidth: window.innerWidth,
      widthPercentage: this.setPercentage(),
    };
  },
  mounted() {
    console.log("moutned");
    this.createNav();
    this.$nextTick(() => {
      window.addEventListener("resize", this.onResize);
    });
    this.widthPercentage = this.setPercentage();
    window.scrollTo(0, 0);
  },
  methods: {
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
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    onSubmit() {
      console.log("submit form: "+this.formMsg);
      this.$router.push({ path: 'search', query: { search: this.formMsg } })
    },
    //used for test
    baseurl(subject) {
      subject_abbrev = "https://apps.ualberta.ca/catalogue/course/";
      subject_abbrev += subject.split().join("_");
      console.log(subject_abbrev);
    },
    //detect screen size
    onResize() {
      this.windowWidth = window.innerWidth;
    },
    //set box width correspond to screen size
    setPercentage() {
      if (this.windowWidth > 1100) {
        return "30%";
      } else if (this.windowWidth > 900) {
        return "40%";
      } else if (this.windowWidth > 600) {
        return "60%";
      } else {
        return "80%";
      }
    },
  },
  watch: {
    windowWidth(newWidth, oldWidth) {
      console.log(newWidth);
      this.widthPercentage = this.setPercentage();
    },
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.onResize);
  },
};
</script>

<style rel="stylesheet/scss" lang="scss">
.search_box {
  padding-top: 10px;
  background-color: #545c64;
  padding-left: 8%;
}
.expand_menu {
  height: 100vh;
}
.expand-container {
  height: 100vh;
}
.el-drawer__body {
  height: 100%;
  box-sizing: border-box;
  overflow-y: auto;
  overflow-x: hidden;
}
// .drawer-affix {
//   position: -webkit-sticky; /* Required for Safari */
//   position: sticky;
//   height: 100vh;
// }
</style>

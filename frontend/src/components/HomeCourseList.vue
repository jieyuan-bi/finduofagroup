<template>
  <el-container>
    <el-col :span="24" v-if="classes.length<200">
      <el-row v-if="classes=={}">
        no courses
      </el-row>
      <el-row v-for="i in classes" :key="i" style="margin-left:8%; margin-top:2%; margin-right:8%;">
        <el-card class="box-card" shadow="hover" style="width: 95vw;" :body-style="{}">
          <div>
            <img src="#" alt="暂无群聊" style="position:relative; float:right;margin-right:2%; width:100px; height:100px;"/>
            <h2>{{i[0]}}</h2>
          </div>
          <div style="margin-top:1%">
            <strong>{{i[1]}}</strong>
          </div>
          <div>
            <el-button type="success" style="margin:2%">加入</el-button>
            <el-button type="info" style="margin:2%">旁观</el-button>
          </div>
          <div style="margin-top:1%">
          <el-collapse>
            <el-collapse-item title="简介" name="1">
              <div>{{i[2]}}</div>
            </el-collapse-item>
          </el-collapse>
          </div>
        </el-card>
      </el-row>
    </el-col>
    <el-col :span="24" v-else-if="classes.length>=200">
      数据过多，无法显示
    </el-col>
    <el-col :span="24" v-else>
      无数据
    </el-col>
  </el-container>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      subject_slug: this.$route.params.subject,
      search_query: this.$route.query.search,
      classes: {},
    };
  },
  mounted() {
    this.initClass();
  },
  methods: {
    initClass() {
      axios
        .get("/api/courses/courses", {
          params: { subject_slug: this.subject_slug , query: this.search_query}
        }, {
          timeout:3000
        })
        .then((response) => {
          this.classes = response.data.classes;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  watch: {
    $route(to, from) {
      this.search_query = this.$route.query.search,
      console.log("route to param:"+to.params.subject+"route query: "+to.query.search);
      // console.log("query: "+this.search_query);
      this.subject_slug = to.params.subject;
      this.initClass()
    },
  },
};
</script>

<style rel="stylesheet/scss" lang="scss">
div.el-col {
  overflow: hidden;
}
</style>
<template>
    <el-container>
      <div>
      <el-aside width="25px"><menu-tab/></el-aside>
      </div>
      <div class="home_main">
      <el-main><course-list/></el-main>
      </div>
  </el-container>
</template>


<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import MenuTab from '../components/HomeMenuTab.vue'
import CourseList from '../components/HomeCourseList.vue'

export default {
  name: 'Home',
  components: {
    MenuTab,
    CourseList,
  },
  methods:{
    checkLogin(){
      if(this.$route.params.login){
        window.location.reload();
      }
    }
  },
  mounted(){
    // console.log('home mount')
    this.checkLogin();
  }
  // watch: {
  //   $route(to, from) {
  //     console.log(to.params.subject)
  //   }
  // }
}
</script>

<style rel="stylesheet/scss" lang="scss">

header.el-aside {
  background-color: yellow;
}


.home_main{
  display: flex;
  align-items: center;
}
  
</style>
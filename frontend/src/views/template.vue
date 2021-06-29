<template>

</template>


<script>
// @ is an alias to /src
import axios from "axios";

export default {
  name: "Manage",
  data() {
    return {
      name: "",
    };
  },
  components: {},
  methods: {
      init(){
          console.log('init')
      }
  },
  mounted() {
    console.log("mounted");
  },
};
</script>

<style rel="stylesheet/scss" lang="scss">
</style>
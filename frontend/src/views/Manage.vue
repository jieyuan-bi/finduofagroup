<template>
  <div v-if="this.$store.state.token>1" class="container" style="margin-top:20px">
    <div class="input-group">
      <div class="form-outline">
        <input type="search" id="form1" class="form-control" v-model="search"/>
        <label class="form-label" for="form1">Search</label>
      </div>
      <button type="button" class="btn btn-success" title="查询" @click="searchUser()">
        <i class="fas fa-search"></i>
      </button>
      <button type="button" class="btn btn-info" style="margin-left:2%" @click="initUsers()">显示全部</button>
    </div>
    <div class="form-check form-switch">
      <input class="form-check-input" type="checkbox" id="flexSwitch" @click="filterUser()"/>
      <label class="form-check-label" for="flexSwitch">只显示未验证用户</label>
    </div>
    <div
      v-for="user in users"
      :key="user.name"
      class="card"
      style="width: 250px; position:relative; float:left;"
    >
      <div class="card-body" v-if="filter==false || (filter==true && user.role==0) ">
        <h5 class="card-title">{{user.name}}</h5>
        <div>
          <button
            type="button"
            class="btn btn-outline-primary"
            :aria-controls="user.name"
            @click="checkDetail(user)"
          >
            <i class="fas fa-info-circle"></i>details
          </button>
        </div>
        <div>
          <button type="button" class="btn btn-outline-success" style="margin-top:5px" @click="confirm(user.name)">验证onecard</button>
          <MDBModal :id="name" tabindex="-1" :labelledby="name" v-model="detailModal">
            <MDBModalHeader>
              <MDBModalTitle :id="name">用户名: {{name}}</MDBModalTitle>
            </MDBModalHeader>
            <MDBModalBody>
              <p>gender: {{gender}}</p>
              <p>major: {{major}}</p>
              <p>role: {{role}}</p>
              <p>email: {{email}}</p>
              <p>wechat: {{wechat}}</p>
              <p>phone: {{phone}}</p>
              <p>create_time: {{create_time}}</p>
              <p>
                onecard:
                <img v-bind:src="onecard" class="card-img-top" alt="..." />
              </p>
            </MDBModalBody>
            <MDBModalFooter>
              <MDBBtn color="secondary" @click="detailModal = false">Close</MDBBtn>
            </MDBModalFooter>
          </MDBModal>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
// @ is an alias to /src
import axios from "axios";
import {
  MDBModal,
  MDBModalHeader,
  MDBModalTitle,
  MDBModalBody,
  MDBModalFooter,
  MDBBtn,
} from "mdb-vue-ui-kit";
import { ref } from "vue";
export default {
  name: "Manage",
  data() {
    return {
      users: [],
      filter:false,
      search:"",
      name: "",
      email: "",
      wechat: "",
      phone: "",
      onecard: "",
      create_time: "",
      gender: "",
      major: "",
      role: "",
    };
  },
  setup() {//set up dialogue box
    const detailModal = ref(false);

    return {
      detailModal,
    };
  },
  components: {
    MDBModal,
    MDBModalHeader,
    MDBModalTitle,
    MDBModalBody,
    MDBModalFooter,
    MDBBtn,
  },
  methods: {
      //confirm to change role
      confirm(username) {
        this.$confirm('此操作将通过用户onecard验证, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {//尝试改变role，后端发生报错则验证失败
            axios
            .post('/api/users/confirmonecard',{name:username})
            .then((response) => {
                if (response.data.success==0){
                    this.$message({
                        type: 'error',
                        message: '验证失败，未知错误!'
                    });
                }else{
                    this.$message({
                        type: 'success',
                        message: '验证通过!'
                    });
                    window.location.reload();
                }
            })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消验证'
          });
        });
      },
      //render all the users
    initUsers() {
      //check if the role is proper
      if (this.$store.state.token > 1) {
        //   console.log("user: ",this.$store.state.account)
        axios
          .get("/api/users/getusers")
          .then((response) => {
            this.users = response.data.users;
            // console.log(this.users[0]);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    //check the user detail, set up data
    checkDetail(user) {
      this.detailModal = true;
      this.name = user.name;
      this.email = user.email;
      this.wechat = user.wechat;
      this.phone = user.phone;
      this.onecard = user.onecard;
      this.create_time = user.create_time;
      this.gender = user.gender;
      this.major = user.major;
      this.role = user.role;
    },
    //filter users by role
    filterUser(){
        this.filter = !this.filter;
    },
    //search specific users
    searchUser(){
        axios
        .get('/api/users/adminsearch',{params:{query:this.search}})
        .then((response) => {
            this.users = response.data.users;
            this.search="";
            // console.log(this.users[0]);
          })
          .catch((error) => {
            console.log(error);
          });
    },
  },
  mounted() {
    this.initUsers();
    console.log("mounted");
  },
};
</script>

<style>
.card {
  margin: 1%;
}

.fa-info-circle {
  color: rgb(255, 215, 106);
}
</style>
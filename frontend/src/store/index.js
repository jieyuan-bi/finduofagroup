import { createStore } from 'vuex'
import createPersistedState from "vuex-persistedstate"

export default createStore({
  state: {
    // set a token to distinct log in roles
    token:-1,
    account:''
  },
  mutations: {
    user (state) {
      state.token=1
    },
    admin (state) {
      state.token=2
    },
    guest (state) {
      state.token=0
    },
    login(state,data){
      state.token = data.role;
      state.account = data.account;
    },
    logout (state) {
      state.token=-1
      state.accout=''
    },
  },
  actions: {
  },
  modules: {
  },
  plugins: [createPersistedState({
    storage: window.sessionStorage,
})],
})

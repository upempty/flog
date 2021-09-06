import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin: false,
    user: 'guest',
  },
  getters: {
    isLogin: state => state.isLogin,
    user: state => state.user
  },
  mutations: {
    userStatus (state, flag) {
      //state.isLogin = flag
      state.user = flag
    }
  },
  //dispatcher
  actions: {
    setUser ({commit}, flag) {
      commit('userStatus', flag)
    }
  }
})

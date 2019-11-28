<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link><span>|</span>
      <router-link to="/movies">Movies</router-link><span>|</span>
      <router-link v-if="!this.$session.get('jwt')" to="/login">Login</router-link> 
      <router-link v-if="this.$session.get('jwt')" to="/logout">Logout</router-link><span>|</span>
      <router-link to="/user">MyPage</router-link><span>|</span>
      <router-link to="/adminmovie">Admin-Movie</router-link><span>|</span>
      <router-link to="/adminuser">Admin-User</router-link>
    </div>
    <div class="row justify-content-center">
      <router-view />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'app',
  data() {
    return {
      checker: false,
    }
  },
  methods: {
    userChecker() {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.get('http://127.0.0.1:8000/api/v1/users/checker/', options)
      .then(res => {
        this.checker = res.data
        console.log(checker)
      })
    },
  },
  mounted() {
    this.userChecker()
  }
}

</script>

<style>
/* #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>

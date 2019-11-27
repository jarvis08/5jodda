<template>
  <div class="5jodda-loginform">
    <h2 class="text-white font-weight-bold mb-8">Log-in</h2>
      <label for="signupId" class="text-white">ID</label>
      <input v-model="credentials.username" type="text" id="signupId" class="form-control" placeholder="ID를 입력하세요.">
      <br>
      <label for="password" class="text-white">Password</label>
      <input v-model="credentials.password" type="password" id="password" class="form-control" placeholder="비밀번호를 입력하세요.">
    <v-btn @click="login" class="blue white--text mt-3">Go!</v-btn>
    <!-- <button @click="login" class="btn btn-primary">Log-in</button> -->
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'


export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {}
    }
  },
  methods: {
    login() {
      axios.post('http://127.0.0.1:8000/api-token-verify/', this.credentials)
      .then(res => {
        this.$session.start()
        this.$session.set('jwt', res.data.token)
        router.push('/')
      })
    },
  }
}
</script>

<style>

</style>
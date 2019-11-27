<template>
  <div class="5jodda-signup">
    <h2 class="text-white font-weight-bold mb-8">Sign-up</h2>
    <div class="form-group">
      <label for="loginId" class="text-white">ID</label>
      <input v-model="credentials.username" type="text" id="loginId" class="form-control" placeholder="ID를 입력하세요.">
      <br>
      <label for="email" class="text-white">Email</label>
      <input v-model="credentials.email" type="text" id="email" class="form-control" placeholder="E-mail 주소를 입력하세요.">
      <br>
      <label for="password" class="text-white">Password</label>
      <input v-model="credentials.password1" type="password" id="password1" class="form-control" placeholder="비밀번호를 입력하세요.">
      <br>
      <label for="password" class="text-white">Password again</label>
      <input v-model="credentials.password2" type="password" id="password2" class="form-control" placeholder="비밀번호를 한번 더 입력하세요.">
      <!-- <button @click="signup" class="btn btn-primary">signup</button> -->
      <v-btn @click="signup" class="green mt-3 white--text">Sign-up</v-btn>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

export default {
  name: 'Signup',
  data() {
    return {
      credentials: {}
    }
  },
  methods: {
    signup() {
      axios.post('http://127.0.0.1:8000/rest-auth/registration/', this.credentials)
      .then(res => {
        this.$session.start()
        this.$session.set('jwt', res.data.token)
        router.push('/')
      })
    },
  },
}
</script>

<style>

</style>
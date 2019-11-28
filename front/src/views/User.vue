<template>
  <v-container col-6 white--text>
    <h2 class="text-center my-12">My Page</h2>
    <div>
      <label for="userName" class="title mt-12">사용자이름</label>
      <p class="form-control">{{ user.username }}</p>
      <label for="userEmail" class="title mt-12">이메일</label>
      <p class="form-control">{{ user.email }}</p>
    </div>
  </v-container>

</template>

<script>
import jwtDecode from 'jwt-decode'
import axios from 'axios'

export default {
  data() {
    return {
      user: {}
    }
  },
  methods: {
    getUser() {
      const token = this.$session.get('jwt')
      const user_id = jwtDecode(token).user_id
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.get(`http://127.0.0.1:8000/api/v1/users/${ user_id }/`, options)
      .then(res => {
        this.user = res.data
      })
    },
  },
  mounted() {
    this.getUser()
  }
}
</script>

<style>

</style>
<template>
  <div>
    <h2>My Page</h2>
    <p>name {{ user.username }}</p>
    <p>email {{ user.email }}</p>
  </div>

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
        console.log(this.user)
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
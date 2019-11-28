<template>
  <v-container col-4>
    <UserList :users="users"/>
  </v-container>
</template>

<script>
import UserList from '@/components/UserList'
import axios from 'axios'

export default {
  name: 'AdminUser',
  data() {
    return {
      users: [],
    }
  },
  components: {
    UserList,
  },
  methods: {
    getUsers() {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      axios.get('http://127.0.0.1:8000/api/v1/users/', options)
      .then(res => {
        this.users = res.data
      })
    },
  },
  mounted() {
    console.log(this.users)
    this.getUsers()
  }
}
</script>

<style>

</style>
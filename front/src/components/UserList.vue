<template>
  <div class="5jodda-userlist text-center">
    <h2 class="m-5 white--text">유저 목록</h2>
    <table class="table table-striped">
      <thead>
        <tr class="white--text">
          <th scope="col">#</th>
          <th scope="col">user_name</th>
          <th scope="col">delete</th>
        </tr>
      </thead>
      <tbody v-for="user in users" :key="user.pk">
        <tr>
          <th scope="row" class="grey--text">{{ user.pk }}</th>
          <td class="light-green--text">{{ user.username }}</td>
          <td><v-btn @click="deleteUser(user.pk)" small dark class="deep-orange--text">delete</v-btn></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

export default {
  name: 'UserList',
  props:{
    users: {
      type: Array
    }
  },
  methods: {
    deleteUser(userPk) {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      axios.post(`http://127.0.0.1:8000/api/v1/users/${ userPk }/delete/`, options)
      .then(
        router.push('/adminuser')
      )
    },
  }
}
</script>

<style>

</style>
<template>
  <div>
    <div class="white--text py-12">
      <label for="userName" class="title">사용자이름</label>
      <input class="form-control" v-model="targetUser.username">
      <label for="userEmail" class="title mt-6">이메일</label>
      <input class="form-control" v-model="targetUser.email">
    </div>
    <div class="5jodda-userlist text-center">
      <h2 class="m-5 white--text">유저 목록</h2>
      <table class="table table-striped">
        <thead>
          <tr class="white--text">
            <th scope="col">#</th>
            <th scope="col">유저이름</th>
            <th scope="col">자세히</th>
            <th scope="col">삭제</th>
          </tr>
        </thead>
        <tbody v-for="user in users" :key="user.pk">
          <tr>
            <th scope="row" class="grey--text">{{ user.pk }}</th>
            <td class="light-green--text">{{ user.username }}</td>
            <td><v-btn @click="getUser(user.pk)" small dark class="deep-green--text">자세히</v-btn></td>
            <td><v-btn @click="deleteUser(user.pk)" small dark class="deep-orange--text">삭제</v-btn></td>
          </tr>
        </tbody>
      </table>
    </div>
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
  data() {
    return {
      targetUser: {}
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
    getUser(target) {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.get(`http://127.0.0.1:8000/api/v1/users/${ target }/`, options)
      .then(res => {
        this.targetUser = res.data
      })
    },
  }
}
</script>

<style>

</style>
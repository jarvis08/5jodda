<template>
  <v-container col-4 class="white--text justify-center mt-12">
    <h2 class="mb-3 text-center">My Page</h2>
    <label for="userName">사용자 이름</label>
    <p class="form-control">{{ user.username }}</p>
    <label for="email">이메일 주소</label>
    <p class="form-control">{{ user.email }}</p>
    <br>
    <h4 class="mt-6">리뷰 목록</h4>
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">content</th>
          <th scope="col">작성자</th>
          <th scope="col">delete</th>
        </tr>
      </thead>
      <tbody v-for="(review, index) in user.review_set" :key="review.pk">
        <tr>
          <th scope="row">{{ index + 1 }}</th>
          <td>{{ review.content }}</td>
          <td>{{ review.user_id }}</td>
          <td><button>delete</button></td>
        </tr>
      </tbody>
    </table>
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
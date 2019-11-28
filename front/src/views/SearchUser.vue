<template>
  <v-container col-4 class="white--text justify-center mt-12">
    <h2 class="mb-3 text-center">My Page</h2>
    <label for="userName">사용자 이름</label>
    <p class="form-control">{{ user.username }}</p>
    <label for="email">이메일 주소</label>
    <p class="form-control">{{ user.email }}</p>
    <br>
    <h4 class="mt-6">리뷰 목록</h4>
    <table class="table table-striped white--text">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">내용</th>
          <th scope="col">삭제</th>
        </tr>
      </thead>
      <tbody v-for="(review, index) in user.review_set" :key="review.pk">
        <tr>
          <th scope="row">{{ index + 1 }}</th>
          <td>{{ review.content }}</td>
          <td><v-btn small dark class="deep-orange--text">삭제</v-btn></td>
        </tr>
      </tbody>
    </table>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      user: {},
      userNum: 0
    }
  },
  methods: {
    getUser() {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.get(`http://127.0.0.1:8000/api/v1/users/${ this.userNum }/`, options)
      .then(res => {
        this.user = res.data
      })
    },
  },
  mounted() {
    this.userNum = this.$route.params.userNum 
    this.getUser()
  }
}
</script>

<style>

</style>
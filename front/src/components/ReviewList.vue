<template>
  <v-layout justify-center align-center>
    <div class="5jodda-reviewlist white--text mt-5">
      <h2>리뷰 목록</h2>
      <table class="table table-striped white--text">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">내용</th>
            <th scope="col">삭제</th>
          </tr>
        </thead>
        <tbody v-for="(review, index) in reviewSet" :key="review.pk">
          <tr>
            <th scope="row">{{ index + 1 }}</th>
            <td>{{ review.content }}</td>
            <td><v-btn @click="deleteReview(review.pk)" small dark class="deep-orange--text">삭제</v-btn></td>
          </tr>
        </tbody>
      </table>
    </div>
  </v-layout>
</template>

<script>
import router from '@/router'
import axios from 'axios'

export default {
  name: 'ReviewList',
  props: {
    users: {
      type: Array,
    },
    reviewSet: {
      type: Array,
    },
    movieNum: {
      type: Number,
    },
  },
  methods: {
    deleteReview(reviewNum) {
      const token = this.$session.get('jwt')
      const temp = Number(this.movieNum)
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      axios.delete(`http://127.0.0.1:8000/api/v1/movies/${ temp }/${ reviewNum }/`, options)
      .then(
        router.push(`/movie/${ temp }`)
      )
    },
  },
}
</script>

<style>

</style>
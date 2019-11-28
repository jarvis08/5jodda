<template>
  <v-layout justify-center align-center>
    <div class="5jodda-reviewlist white--text mt-5">
      <h2>리뷰 목록</h2>
      <table class="table table-striped white--text">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">content</th>
            <th scope="col">작성자</th>
            <th scope="col">delete</th>
          </tr>
        </thead>
        <tbody v-for="(review, index) in reviewSet" :key="review.pk">
          <!-- <tr>
            <th scope="row"></th>
            <td>{{ review.contnet }}</td>
            <td><button>{{ review.user.username }}</button></td>
            <td><button>update</button></td>
          </tr> -->
          <tr>
            <th scope="row">{{ index + 1 }}</th>
            <td>{{ review.content }}</td>
            <td>{{ review.user_id }}</td>
            <td><button @click="deleteReview(review.pk)">delete</button></td>
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
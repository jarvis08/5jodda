<template>
  <div class="5jodda-reviewinput">
    <h2>리뷰 남기기</h2>
    <input type="text" v-model="reviewContent">
    <input type="text" v-model="reviewScore">
    <button @click="postReview">submit</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewInput',
    data() {
    return {
      reviewContent: '1',
      reviewScore: 5,
    }
  },
  props: {
    movieNum: {
      type: Number,
    }
  },
  methods: {
    postReview() {
      const token = this.$session.get('jwt')
      console.log(this.reviewContent)
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/api/v1/movies/${ this.movieNum }/`,
        headers: {
          Authorization: 'JWT ' + token,
        }, 
        data: {
          content: this.reviewContent,
          score: this.reviewScore,
        }
      }
      )
      // .then(
      //   // 새로고침
      // )
    },
  }
}
</script>

<style>

</style>
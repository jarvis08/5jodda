<template>
  <v-layout mt-12 justify-center align-center>
    <div class="5jodda-reviewinput d-inline-block white--text">
      <h2>리뷰 남기기</h2>
      <input type="text" id="review-content" v-model="reviewContent" class="form-control" placeholder="내용">
      <input type="number" id="review-score" v-model="reviewScore" class="form-control d-inline mt-1" placeholder="점수">
      <v-btn @click="postReview" class="ml-5 blue white--text">등록</v-btn>
    </div>
  </v-layout>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewInput',
    data() {
    return {
      reviewContent: '',
      reviewScore: 10,
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
      ).then(
        this.$emit('inputReview')
      )
    },
  }
}
</script>

<style>

</style>
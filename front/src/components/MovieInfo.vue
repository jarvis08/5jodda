<template>
<v-layout>
  <div class="5jodda-movieinfo white--text text-center d-flex justify-content-center">
    <div class="col-6">
      <h2>{{ movie.title }}</h2>
      <div>
        <span v-for="genre in movie.genres" :key="genre.id" class="btn-sm btn-dark ml-1">{{ findGenre(genre) }}</span>
      </div>
      <img :src=movie.poster_url :alt="`${ movie.title }의 포스터`" class="card-img-top col-6">
      <p class="text-start">{{ movie.description }}</p>
      <v-btn @click="deleteMovie" small dark class="deep-orange--text">영화 삭제</v-btn>
      <v-btn small dark class="ml-1 green--text">영화 수정</v-btn>
    </div>
  </div>
  </v-layout>
</template>

<script>
import router from '@/router'
import axios from 'axios'

export default {
  name: 'MovieInfo',
  data() {
    return {
      genres2: []
    }
  },
  props: {
    movie: {
      type: Object,
    },
  },
  methods: {
    deleteMovie() {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      axios.delete(`http://127.0.0.1:8000/api/v1/movies/${ this.movie.pk }/`, options)
      .then(
        router.push('/movies')
      )
    },
    findGenre(genreNum) {

      const genreName = this.genres2[genreNum-1]

      return genreName
    },
    getGenres() {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.get('http://127.0.0.1:8000/api/v1/movies/genres/', options)
      .then(res => {
        res.data.forEach(element => {
          this.genres2.push(element.name)
        });
      })
    },
  },
  mounted() {
    this.getGenres()
  }
}
</script>

<style>

</style>
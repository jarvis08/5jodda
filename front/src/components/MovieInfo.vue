<template>
  <div class="5jodda-movieinfo" >
    <h2>영화 정보</h2>
    
    <h3>{{ movie.title }}</h3>
    <img :src=movie.poster_url :alt="`${ movie.title }의 포스터`" class="card-img-top">
    <h4>영화 정보</h4>
    <p>{{ movie.description }}</p>
    <p>genres</p>
    <span v-for="genre in movie.genres" :key="genre.id" class="btn-sm btn-dark">{{ findGenre(genre) }}</span>
    <p>like_users</p>
    
  </div>
</template>

<script>
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
<template>
  <div class="5jodda-movielist">
    <h2>전체 리스트</h2>
    <div class="row container">
    <div v-for="movie in movies" :key="movie.pk" class="cal-3" >
      <div class="card border-dark m-3" style="width: 18rem;">
        <a :href="`/movie/${ movie.pk }`"><img :src=movie.poster_url :alt="`${ movie.title }의 포스터`" class="card-img-top"></a>
        <div class="card-body text-center border-dark">
          <h5 class="card-title">{{ movie.title }}</h5>
          <span v-for="genre in movie.genres" :key="genre.id" class="btn-sm btn-dark">{{ findGenre(genre) }}</span>
        </div>
      </div>

    </div>

    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {

  name: 'MovieList',
  data() {
    return {
      genres2: []
    }
  },
  props: {
    movies: {
      type: Array,
    },
    genres: {
      type: Array,
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
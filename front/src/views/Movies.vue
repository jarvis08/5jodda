<template>
  <div class="5jodda-movie">
    <h1 class="white--text text-center m-5">오질걸?</h1>
    <MovieRec />
    <MovieList :movies="movies" />
  </div>
</template>

<script>
import MovieRec from '@/components/MovieRec'
import MovieList from '@/components/MovieList'
import axios from 'axios'

export default {
  name: 'Movies',
  components: {
    MovieRec,
    MovieList,
  },
  data() {
    return {
      movies: [],
      genres: [],
    }
  },
  methods: {
    getMovies() {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.get('http://127.0.0.1:8000/api/v1/movies/', options)
      .then(res => {
        this.movies = res.data
      })
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
          this.genres.push(element.name)
        });
      })
    },
  },
  mounted() {
    this.getGenres()
    this.getMovies()
  }
}
</script>

<style>

</style>
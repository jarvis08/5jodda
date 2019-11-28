<template>
  <div class="5jodda-movie">
    <h1 class="white--text text-center m-5">영화 검색</h1>
    <MovieRec />
    <label for="genres" class="text-white mt-3 d-block">장르를 선택하세요.</label>
    <span v-for="genre in genres2" :key="genre.pk" class="text-white d-inline mr-3">
      <input type="checkbox" :id="genre.name" :value="genre.pk" v-model="selectGenres">
      <label :for="genre.name">{{ genre.name }}</label>
    </span>
    <v-btn @click="selectMovie(selectGenres)" class="green white--text mt-3" small>선택</v-btn>
    <MovieList :selectGenres="selectGenres" :movies="movies" />
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
import axios from 'axios'

export default {
  name: 'Movies',
  components: {
    MovieList,
  },
  data() {
    return {
      movies: [],
      genres: [],
      genres2: [],
      selectGenres: [],
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
        this.genres2 = res.data
        res.data.forEach(element => {
          this.genres.push(element.name)
        });
      })
    },
    selectMovie(genreNum) {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.get(`http://127.0.0.1:8000/api/v1/movies/select_genres/${genreNum}/`, options)
      .then(res => {
        this.movies = res.data
      })
    },
  },
  mounted() {
    this.getGenres()
    this.getMovies()
  },
}
</script>

<style>

</style>
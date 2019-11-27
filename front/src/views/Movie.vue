<template>
  <div class="5jodda-movie">
    <MovieInfo :movie="movie"/>
    <ReviewInput :movieNum="movieNum"/>
    <ReviewList :users="users" :reviewSet="movie.review_set"/>
  </div>
</template>

<script>
import MovieInfo from '@/components/MovieInfo'
import ReviewInput from '@/components/ReviewInput'
import ReviewList from '@/components/ReviewList'
import axios from 'axios'

export default {
  name: 'Movie',
  components: {
    MovieInfo,
    ReviewInput,
    ReviewList,
  },

  data() {
    return {
      movieNum: 0,
      movie: [],
      genres: [],
      users: [],
    }
  },

  methods: {
    getMovie() {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      axios.get(`http://127.0.0.1:8000/api/v1/movies/${ this.movieNum }` , options)
      .then(res => {
        this.movie = res.data
        
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
    getUsers() {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.get('http://127.0.0.1:8000/api/v1/users/', options)
      .then(res => {
        this.users = res.data
      })
    },
  },
  mounted(){
    this.movieNum = this.$route.params.movieNum 
    this.getMovie()
    this.getUsers()
  },
}
</script>

<style>

</style>
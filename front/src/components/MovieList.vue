<template>
  <v-layout row wrap justify-center align-center>
      <div v-for="movie in movies" :key="movie.pk" class="m-3 hover-dark">
        <v-hover v-slot:default="{ hover }" :open-delay="0" :close-delay="0" :value="false">
        <a :href="`/movie/${ movie.pk }`"><v-card :elevation="hover ? 12 : 2" color="#424242" class="mx-auto" width="18rem">
          <v-img class="white--text align-end" :src=movie.poster_url :alt="`${ movie.title }의 포스터`" max-height="25rem"></v-img>
          <v-card-title class="white--text" style="text-overflow: ellipsis;">{{ movie.title }}</v-card-title>
          <div class="d-flex justify-center pb-1">
            <v-btn small v-if="!movie.genres.length" color="black" class="white--text">없음</v-btn>
            <v-btn small v-for="genre in movie.genres" :key="genre.id" color="black" class="ml-1 white--text font-weight-light">{{ findGenre(genre) }}</v-btn>
          </div>
        </v-card></a></v-hover>
      </div>
      <!-- <div class="card border-dark m-3" style="width: 18rem;">
        <a :href="`/movie/${ movie.pk }`"><img :src=movie.poster_url :alt="`${ movie.title }의 포스터`" class="card-img-top"></a>
        <div class="card-body text-center border-dark">
          <h5 class="card-title">{{ movie.title }}</h5>
          <span v-for="genre in movie.genres" :key="genre.id" class="btn-sm btn-dark">{{ findGenre(genre) }}</span>
        </div>
      </div> -->
    </v-layout>
</template>

<script>
import axios from 'axios'

export default {

  name: 'MovieList',
  data() {
    return {
      genres2: [],
    }
  },
  props: {
    movies: {
      type: Array,
    },
    genres: {
      type: Array,
    },
    selectGenres: {
      type: Array,
    }
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
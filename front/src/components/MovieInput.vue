<template>
  <div class="5jodda-movieinput">
    <h2 class="text-white font-weight-bold mb-8 text-center">새 영화</h2>
    <label for="moviePk" class="text-white mt-3">영화 번호</label>
    <input v-model="Info.pk" type="text" id="moviePk" class="form-control" placeholder="영화 번호를 입력하세요.">
    <label for="movieTitle" class="text-white mt-3">영화명</label>
    <input v-model="Info.title" type="text" id="movieTitle" class="form-control" placeholder="영화 제목을 입력하세요.">
    <label for="audience" class="text-white mt-3">누적관객수</label>
    <input v-model="Info.audience" type="text" id="audience" class="form-control" placeholder="누적관객수를 입력하세요.">
    <label for="posterUrl" class="text-white mt-3">포스터 URL</label>
    <input v-model="Info.posterUrl" type="text" id="posterUrl" class="form-control" placeholder="포스터 URL을 입력하세요.">
    <label for="description" class="text-white mt-3">줄거리</label>
    <input v-model="Info.description" type="text" id="description" class="form-control" placeholder="줄거리를 입력하세요.">
    <label for="genres" class="text-white mt-3 d-block">장르를 선택하세요.</label>
    <div v-for="genre in genres2" :key="genre.pk" class="text-white d-inline mr-3">
      <input type="checkbox" :id="genre.name" :value="genre.pk" v-model="genres">
      <label :for="genre.name">{{ genre.name }}</label>
    </div>
    <br>
    <v-btn @click="createMovie()" class="blue white--text mt-3">등록하기</v-btn>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieInput',
  data() {
    return {
      Info: {},
      genres: [],
      genres2: [],
      checkedNames: []
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
        this.genres2 = res.data
        })
    },
    createMovie() {
      const token = this.$session.get('jwt')
      const inputData = this.Info
      inputData.genres = this.genres
      
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/v1/movies/create/',
        data: inputData,
        headers: {
          Authorization: 'JWT ' + token
        }
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
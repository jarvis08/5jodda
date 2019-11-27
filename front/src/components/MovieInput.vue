<template>
  <div class="5jodda-movieinput">
    <h2>영화 생성</h2>
    <div class="form-group">
      <label for="title">영화번호</label>
      <input v-model="Info.pk" type="text" id="movie_pk" class="form-control" placeholder="영화 번호 입력하세요.">
      <br>
      <label for="title">영화명</label>
      <input v-model="Info.title" type="text" id="title" class="form-control" placeholder="영화 제목을 입력하세요.">
      <br>
      <label for="audience">누적관객수</label>
      <input v-model="Info.audience" type="text" id="audience" class="form-control" placeholder="누적관객수를 입력하세요.">
      <br>
      <label for="posterUrl">포스터 URL</label>
      <input v-model="Info.posterUrl" type="text" id="posterUrl" class="form-control" placeholder="포스터 URL을 입력하세요.">
      <br>
      <label for="description">줄거리</label>
      <input v-model="Info.description" type="text" id="description" class="form-control" placeholder="줄거리를 입력하세요.">
      <br>
      <label for="genres">장르</label>
      <div v-for="genre in genres2" :key="genre.pk" >
        <input type="checkbox" :id="genre.name" :value="genre.pk" v-model="genres">
        <label :for="genre.name">{{ genre.name }}</label>
      </div>

      <br>
      <button @click="createMovie()" class="btn btn-primary">등록하기</button>
    </div>
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
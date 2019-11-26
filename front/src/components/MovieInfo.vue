<template>
  <div class="5jodda-movieinfo" >
    <h2>영화 정보</h2>
    
    <h3>{{ movie.title }}</h3>
    
  </div>
</template>

<script>
export default {
  name: 'MovieInfo',
  data() {
    return {
    }
  },
  props: {
    movie: {
      type: Array,
    },
  },
  methods: {

  },
  watched: {

  }
}
</script>

<style>

</style>
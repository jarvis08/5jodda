<template>
  <v-container col-10 text-center>
    <img
      src="http://image.chosun.com/sitedata/image/201202/08/2012020800627_0.jpg"
      alt="homePoster"
      style="border-radius: 10px; width: 30%;"
    >
    <v-carousel
      cycle
      height="200"
      hide-delimiter-background
      show-arrows-on-hover
      class="mt-5"
    >
      <v-carousel-item
        v-for="(slide, i) in slides"
        :key="i"
      >
        <v-sheet
          :color="colors[i]"
          height="100%"
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
            <div class="display-1">
              <img :src=slide.imageUrl style="height: 200px;" class="mr-5">
              {{ slide.content }}
              <img :src=slide.imageUrl style="height: 200px;" class="ml-5">
            </div>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>
  </v-container>
</template>

<script>
export default {
  name: 'AppInfo',
  data () {
    return {
      colors: [
        'dark',
        'dark',
        'light-green darken-4',
      ],
      slides: {
        s1: {
          content: '좋아하는 장르만 선택하세요.',
          imageUrl: ''
        },
        s2: {
          content: '제가 그럼 영화를..',
          imageUrl: ''
        },
        s3: {
          content: '골라는 드릴게.',
          imageUrl: "https://pbs.twimg.com/profile_images/378800000720268704/ce1ec51825a576fc51753fe4f59e6bf8_400x400.jpeg",
        },
      },
    }
  },
}
</script>

<style>

</style>
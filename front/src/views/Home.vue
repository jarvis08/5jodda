<template>
  <div>
    <h1 class="text-center white--text mt-5">이 영화 오조따!</h1>
    <AppInfo />
  </div>
</template>

<script>
import AppInfo from '@/components/AppInfo'

export default {
  name: 'home',
  components: {
    AppInfo,
  }
}
</script>

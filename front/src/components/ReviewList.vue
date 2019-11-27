<template>
  <div class="5jodda-reviewlist">
    <h2>리뷰 목록</h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">content</th>
          <th scope="col">작성자</th>
          <th scope="col">delete</th>
        </tr>
      </thead>
      <tbody v-for="(review, index) in reviewSet" :key="review.pk">
        <!-- <tr>
          <th scope="row"></th>
          <td>{{ review.contnet }}</td>
          <td><button>{{ review.user.username }}</button></td>
          <td><button>update</button></td>
        </tr> -->
        <tr>
          <th scope="row">{{ index + 1 }}</th>
          <td>{{ review.content }}</td>
          <td>{{ review.user_id }}</td>
          <td><button>delete</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'ReviewList',
  props: {
    users: {
      type: Array,
    },
    reviewSet: {
      type: Array,
    },
  },
}
</script>

<style>

</style>
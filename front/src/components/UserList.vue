<template>
  <div class="5jodda-userlist text-center">
    <h2 class="m-5 white--text">유저 목록</h2>
    <table class="table table-striped">
      <thead>
        <tr class="white--text">
          <th scope="col">#</th>
          <th scope="col">user_name</th>
          <th scope="col">delete</th>
        </tr>
      </thead>
      <tbody v-for="user in users" :key="user.pk">
        <tr>
          <th scope="row" class="grey--text">{{ user.pk }}</th>
          <td class="light-green--text">{{ user.username }}</td>
          <td><v-btn class="deep-orange--text">delete</v-btn></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'UserList',
  props:{
    users: {
      type: Array
    }
  },
}
</script>

<style>

</style>
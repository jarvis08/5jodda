<template>
  <div class="5jodda-userlist">
    <h2>유저 목록</h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">user_name</th>
          <th scope="col">update</th>
          <th scope="col">delete</th>
        </tr>
      </thead>
      <tbody v-for="user in users" :key="user.pk">
        <tr>
          <th scope="row">{{ user.pk }}</th>
          <td>{{ user.username }}</td>
          <td><button>delete</button></td>
          <td><button>update</button></td>
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
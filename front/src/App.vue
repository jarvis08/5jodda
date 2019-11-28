

<template>
  <v-app style="background-color: #212121;">
    <v-app-bar
      app
      color="dark"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Movie Logo"
          class="shrink mr-2"
          contain
          src="https://image.flaticon.com/icons/png/512/83/83519.png"
          transition="scale-transition"
          width="40"
        />
        <span class="headline font-weight-bold">오조따!</span>
        
      </div>
        <v-btn text>
          <router-link to="/" class="text-white">Home</router-link>
        </v-btn>
        <v-btn text>
          <router-link to="/movies" class="text-white">Movies</router-link>
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn text v-if="this.checker">
          <router-link to="/adminmovie" class="text-primary">Admin-Movie</router-link>
        </v-btn>
        <v-btn text v-if="this.checker">
          <router-link to="/adminuser" class="text-primary">Admin-User</router-link>
        </v-btn>
        <v-btn text v-if="this.$session.get('jwt')">
          <router-link to="/user" class="text-white">My Page</router-link>
        </v-btn>
        <v-btn text v-if="!this.$session.get('jwt')">
          <router-link to="/login" class="text-white">Login</router-link>
        </v-btn>
        <v-btn text v-if="this.$session.get('jwt')">
          <router-link to="/logout" class="text-white">Logout</router-link>
        </v-btn>
    </v-app-bar>

    <v-content>
      <v-container>
        <router-view />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import axios from 'axios'

export default {
  name: 'app',
  data() {
    return {
      checker: false,
    }
  },
  methods: {
    userChecker() {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.get('http://127.0.0.1:8000/api/v1/users/checker/', options)
      .then(res => {
        this.checker = res.data
        console.log(this.checker)
      })
    },
  },
  mounted() {
    this.userChecker()
  }
}
</script>

<style>
a.hoverColor:hover {
  color: white;
}
</style>

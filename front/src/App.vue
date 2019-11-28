

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
        <v-spacer></v-spacer>
      </div>
        <v-btn text>
          <router-link to="/" class="text-white">Home</router-link>
        </v-btn>
        <v-btn text>
          <router-link to="/movies" class="text-white">Movies</router-link>
        </v-btn>
        <v-btn text v-if="!this.$session.get('jwt')">
          <router-link to="/login" class="text-white">Login</router-link>
        </v-btn>
        <v-btn text v-if="this.$session.get('jwt')">
          <router-link to="/logout" class="text-white">Logout</router-link>
        </v-btn>
        <v-btn text>
          <router-link to="/adminmovie" class="text-primary">Admin-Movie</router-link>
        </v-btn>
        <v-btn text>
          <router-link to="/adminuser" class="text-primary">Admin-User</router-link>
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

</script>

<style>
</style>

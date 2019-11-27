<template>
  <v-container text-center col-4>
    <LoginForm />
    <br>
    <br>
    <hr style="background-color: white;">
    <Signup class="mt-12"/>
  </v-container>
</template>

<script>
import LoginForm from '@/components/LoginForm'
import Signup from '@/components/Signup'

export default {
    name: 'Login',
    components: {
        LoginForm,
        Signup,
    }
}
</script>

<style>

</style>
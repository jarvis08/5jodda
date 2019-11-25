<template>
  <div class="5jodda-login col-6">
    <LoginForm />
    <Signup class="mt-3"/>
  </div>
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
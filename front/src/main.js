import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueSession from 'vue-session'
import vuetify from './plugins/vuetify';

Vue.use(VueSession)
Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')

import Vue from 'vue'
//importamos la aplicacion
import App from './App'
//importamos la libreria router
import vueRouter from 'vue-router'
//importamos archivo router.js
import router from './router'

//Utilizamos vue router para referenciar las URL
Vue.use(vueRouter)

Vue.config.productionTip = false

new Vue({
    router, //router.js
    el: '#app',
    components: { App },
    template: '<App/>'
})
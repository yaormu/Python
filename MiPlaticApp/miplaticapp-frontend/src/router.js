import vueRouter from 'vue-router'
//Importar un archivo vue
import User from './components/User'
import UserBalance from './components/UserBalance'
import UserAuth from './components/UserAuth'
import UserTransaction from './components/UserTransaction'
import App from './App'

const router = new vueRouter({
    mode: 'history', //forma de cadena 
    base: __dirname, //empieza en el directorio actual
    routes: [{
            path: '/',
            name: "root",
            component: App
        },
        { //Se empiezan agregar componentes a la aplicación, que fueron importados al principio de este archivo
            path: '/user/:username',
            name: "user",
            component: User
        },
        {
            path: '/user/balance/:username',
            name: "user_balance",
            component: UserBalance
        },
        {
            path: '/user/transaction',
            name: "transaction",
            component: UserTransaction
        },
        {
            path: '/user/auth',
            name: "user_auth",
            component: UserAuth
        },
    ]
})

export default router
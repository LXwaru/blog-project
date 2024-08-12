<script>
import axios from 'axios';
import { RouterLink } from 'vue-router';
import { mapGetters, mapActions } from 'vuex'

export default {
    data() {
        return {
            localUsername: '',
            password: '',
            userId: null
        };
    },
    computed: {
        ...mapGetters(['username', 'user']),
        username() {
            return this.user ? this.user.username : this.username
        }
    },
    created() {
        this.$store.dispatch('initializeUser');
    },
    methods: {
        ...mapActions(['loginUser', 'logoutUser']),
        async login() {
            try {
                const response = await axios.post('http://localhost:8000/token', new URLSearchParams({
                username: this.localUsername,
                password: this.password
            }), {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
            }
            });
            if (response.status === 200) {
                const { access_token } = response.data;
                this.loginUser({ username: this.localUsername, token: access_token });
                console.log(response.data)
            } else {
                alert(response.data.detail);
            }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred during login.');
            }
        },
        logout() {
            this.logoutUser();
        }
    }
};
</script>

<template>
    <div v-if="!user">
        <form @submit.prevent="login">
            <h3>Login</h3>
            <input v-model="localUsername" id="username" placeholder="username" />
            <input v-model="password" id="password" type="password" placeholder="password" /><br>
            <button type="submit">Login</button>
            <RouterLink to="CreateAccount"> or Create Account</RouterLink>
        </form>
    </div>
    <div v-else>
        <p>Welcome, {{ username }}! <button @click="logout">logout</button></p>
        
    </div>

</template>



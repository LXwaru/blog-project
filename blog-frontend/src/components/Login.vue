<script>
import axios from 'axios';
import { RouterLink } from 'vue-router';
import { mapGetters, mapActions } from 'vuex'

export default {
    data() {
        return {
            localUsername: '',
            password: '',
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
                const token = response.data.access_token
                this.loginUser({ username: this.localUsername, token });
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
            <h2>Login</h2>
            <input v-model="localUsername" id="username" placeholder="username" /><br>
            <input v-model="password" id="password" type="password" placeholder="password" /><br>
            <button type="submit">Login</button><br>
            <RouterLink to="CreateAccount">Create Account</RouterLink>
        </form>
    </div>
    <div v-else>
        <h1>Welcome, {{ username }}</h1>
        <RouterLink to="ListMyBlogs">My Blogs</RouterLink><br>
        <button @click="logout">logout</button>
    </div>

</template>



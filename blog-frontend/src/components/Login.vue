<script>
import axios from 'axios';
import { RouterLink } from 'vue-router';

export default {
    data() {
        return {
            username: '',
            password: '',
            user: null
        };
    },
    created() {
        const token = localStorage.getItem('access_token');
        const username = localStorage.getItem('username');
        if (token && username) {
            this.user = token;
            this.username = username
        }
    },
    methods: {
        async login() {
            try {
                const response = await axios.post('http://localhost:8000/token', new URLSearchParams({
                username: this.username,
                password: this.password
            }), {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            });
            if (response.status === 200) {
                const token = response.data.access_token
                this.user = token;
                localStorage.setItem('access_token', token);
                localStorage.setItem('username', this.username);
            } else {
                alert(response.data.detail);
            }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred during login.');
            }
        },
        logout() {
            this.user = null;
            this.username = ''
            localStorage.removeItem('access_token')
            localStorage.removeItem('username')
        }
    }
};
</script>

<template>
    <div v-if="!user">
        <form @submit.prevent="login">
            <h2>Login</h2>
            <input v-model="username" id="username" placeholder="username" /><br>
            <input v-model="password" id="password" type="password" placeholder="password" /><br>
            <button type="submit">Login</button><br>
            <RouterLink to="CreateAccount">Create Account</RouterLink>
        </form>
    </div>
    <div v-else>
        <h1>Welcome, {{username}}</h1>
        <RouterLink to="ListMyBlogs">My Blogs</RouterLink><br>
        <button @click="logout">logout</button>
    </div>

</template>



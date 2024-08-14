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
    async mounted() {
        if (this.user) {
            try {
                const token = this.$store.state.user.token;
                const userData = await axios.get('http://localhost:8000/users/me/', {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                })
                this.userId = userData.data.id
            } catch (error) {
                console.error("can't get userData", error)
            }
        }
    },
    computed: {
        ...mapGetters(['username', 'user']),
        username() {
            return this.user ? this.user.username : this.localUsername
            // console.log(user)
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
        async logout() {
            await this.logoutUser();
            this.$router.push('/')
        },
        async deleteAccount() {
            try{
                axios.delete(`http://localhost:8000/api/user/${this.userId}`)
                alert('account successfully deleted')
                await this.logoutUser();
                this.$router.push('/')
            } catch (error) {
                console.error("error deleting account", error)
            }
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
    <div v-else class="some-space">
        <p>Welcome, {{ username }}! <button @click="logout">logout</button></p><br>
        <button @click="deleteAccount">delete my account</button>

        
    </div>

</template>


<style>
form {
    padding: 25px;
}

.some-space {
    padding: 25px;
}
</style>
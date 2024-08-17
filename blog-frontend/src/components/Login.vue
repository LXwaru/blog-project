<script>
import axios from 'axios';
import { RouterLink } from 'vue-router';
import { mapGetters, mapActions } from 'vuex'

export default {
    data() {
        return {
            localUsername: '',
            password: '',
            userId: null,
            accountView: false,
            createUsername: '',
            createPassword: '',
            confirmPassword: ''
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
        },
        passwordsMatch() {
            return this.createPassword === this.confirmPassword;
        }
    },
    created() {
        this.$store.dispatch('initializeUser');
    },
    methods: {
        ...mapActions(['loginUser', 'logoutUser']),
        toggleCreateAccount() {
            this.accountView = !this.accountView
        },
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
                this.loginUser({ username: this.localUsername, token: access_token })
                console.log('login successful', response.data)
                this.$router.push({ name: "home" });
                location.reload();

            } else {
                alert('login failed:', response.data.detail);
            }
            } catch (error) {
                console.error('Error during login:', error.response ? error.response.data : error.message);
                alert('An error occurred during login.');
            }
        },
        async createAccount() {
                if (!this.passwordsMatch) {
                    alert('Passwords do not match');
                    return;
                }
                try {
                    const newUserData = await axios.post('http://localhost:8000/api/users', {
                        username: this.createUsername,
                        password: this.createPassword
                    });
                    console.log(newUserData.data)
                    if (newUserData.status == 200) {
                        alert("account created successfully");
                        accountView = false;
                    } else {
                        alert('Account creation failed: ' + newUserData.data.detail);
                    }
                } catch (error) {
                    console.error("Error during account creation:", error.response ? error.response.data : error.message);
                    alert('An error occurred during account creation');
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
            this.$router.push('/')
        }
    }
};
</script>

<template>
    <div>
        <!-- createAccount Form -->
        <div v-if="accountView">
            <form @submit.prevent="createAccount">
                <h2>Create an account</h2>
                <input v-model="createUsername" id="createUsername" placeholder="username" /><br>
                <input v-model="createPassword" id="createPassword" type="password" placeholder="password" /><br>
                <input v-model="confirmPassword" id="confirmPassword" type="password" placeholder="confirm password" /><br>
                <span v-if="createPassword && confirmPassword && !passwordsMatch" style="color: red;">
                    Passwords do not match
                </span>
                <button type="submit" :disabled="!passwordsMatch">Create Account</button>
            </form>
            <button @click="toggleCreateAccount">back to login</button>
        </div>

        <!-- Login Form -->
        <div v-else>
            <div v-if="!user">
                <form @submit.prevent="login">
                    <h3>Login</h3>
                    <input v-model="localUsername" id="username" placeholder="username" />
                    <input v-model="password" id="password" type="password" placeholder="password" /><br>
                    <button type="submit">Login</button><br>
                </form>
                <button @click="toggleCreateAccount">Create Account</button>         
            </div>
            <div v-else class="some-space">
                <p>Welcome, {{ username }}! <button @click="logout">logout</button></p><br>
                <button @click="deleteAccount">delete my account</button>
            </div>
        </div>
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
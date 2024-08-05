<template>
    <form @submit.prevent="createAccount">
        <h2>Create an account</h2>
        <input v-model="username" id="createUsername" placeholder="username" /><br>
        <input v-model="password" id="createPassword" type="password" placeholder="password" /><br>
        <input v-model="confirmPassword" id="confirmPassword" type="password" placeholder="confirm password" /><br>
        <span v-if="password && confirmPassword && !passwordsMatch" style="color: red;">Passwords do not match</span>
        <button type="submit" :disabled="!passwordsMatch">Create Account</button>
    </form>
</template>


<script>
    import axios from 'axios'
    export default {
        name: 'CreateAccount',
        data() {
            return {
                username: "",
                password: "",
                confirmPassword: ""
            };
        },
        computed: {
            passwordsMatch() {
                return this.password === this.confirmPassword;
            }
        },
        methods: {
            async createAccount() {
                if (!this.passwordsMatch) {
                    alert('Passwords do not match');
                    return;
                }
                try {
                    const newUserData = await axios.post('http://localhost:8000/api/users', {
                        username: this.username,
                        password: this.password
                    });
                    console.log(newUserData.data)
                    if (newUserData.status == 200) {
                        alert("account created successfully");
                        this.$router.push({ name: "home" })
                    } else {
                        alert(newUserDate.data.detail)
                    }
                } catch (error) {
                    console.error("error", error);
                    alert('an error occurred during account creation');
                }
            },
            goToLogin() {
                this.$router.push({ name: "Login" })
            }
        }
    }
</script>
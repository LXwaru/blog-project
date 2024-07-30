<script lang="ts">

export default {
    data() {
        return {
            message: "Login",
            username: "username", 
            password: "password",
            createAccount: "create account",
        }
    }
}
</script>

<template>
    <div>
        <h2>{{message}}</h2>
        <br>
        <input placeholder="username" /><br>
        <input placeholder="password" /><br>
        <button>{{ message }}</button><br>
        <button>{{ createAccount }}</button>
    </div>
</template>



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
        <input id="username" placeholder="username" /><br>
        <input id="password" placeholder="password" /><br>
        <button>{{ message }}</button><br>
        <button>{{ createAccount }}</button>
    </div>
</template>



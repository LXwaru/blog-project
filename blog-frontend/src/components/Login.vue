<script lang="ts">

export default {
    data() {
        return {
            username: "username", 
            password: "password",
        }
    }
}
</script>

<template>
    <div>
        <h2>Login</h2>
        <input id="username" placeholder="username" /><br>
        <input id="password" placeholder="password" /><br>
        <button>Login</button><br>
        <button>Create Account</button>
    </div>

</template>



<script>
export default {
    data() {
        return {
            account: false
        }
    }
}
</script>

<template>
    <div> 
        <h1 v-if="account">Welcome {{ username }}</h1>
        <h1 v-else>Sign up or log in</h1>
        <p v-if="account">here are your blogs!</p>
        <p v-else>here are some other people's blogs</p>
    </div>
</template>
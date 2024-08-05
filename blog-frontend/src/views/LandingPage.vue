<script>
import axios from 'axios'

export default {
    name: "LandingPage",
    data() {
        return {
            user: {}
        }
    },
    async mounted() {

    const currentUserData = await axios.get("http://localhost:8000/users/me")
    console.log(currentUserData)
    }
}

</script>

<template>

</template>
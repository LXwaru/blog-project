<script>
import axios from "axios"
export default {
    name: "app",
    async mounted() 
    {
        let result = await axios.get("http://localhost:8000/api/users/")
        console.warn(result)
    }
}
</script>

<template>
    <h1>all the users</h1>
</template>
<template>
    <div>
        <h1>This particular bloggers blogs</h1>
        <p  v-for="blog in blogs" :key="item.id">
            <RouterLink to="/">{{ blog.title }}</RouterLink>    
        </p>

    </div>
</template>


<script>
import axios from "axios"

export default {
    name: "app",
    data() 
    {
        return {
            blogs: []

        }
    },
    async mounted() {
        try {
            let blogResults = await axios.get("http://localhost:8000/api/users/1/items/");
            console.log(blogResults.data);
            this.blogs = blogResults.data;
        } catch (error) {
            console.error("Error fetching blogs:", error.response ? error.response.data : error.message);
        }
    }
}
</script>

<style>


</style>
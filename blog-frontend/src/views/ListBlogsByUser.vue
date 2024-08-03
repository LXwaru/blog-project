<template>
    <div>
        <h1>{{userId}}'s blogs</h1>
        <p  v-for="blog in blogs" :key="blog.id">
            <RouterLink to="/">{{ blog.title }}</RouterLink>    
        </p>

    </div>
</template>


<script>
import axios from "axios"

export default {
    name: "ListBlogsByUser",
    props: {
        userId: {
            type: [Number, String], 
            required: true
        }
    },
    data() {
        return {
            blogs: []

        }
    },
    async mounted() {
        const userId = Number(this.userId)
        if (isNaN(this.userId)) {
            throw new Error("invalid user ID")
        }
        let blogResults = await axios.get(`http://localhost:8000/api/users/${this.userId}/items/`, {
            params: {
                owner_id: userId
            }
        })
            console.log(blogResults.data);
            this.blogs = blogResults.data;
    }
}
</script>

<style>


</style>
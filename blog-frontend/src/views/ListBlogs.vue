<template>
    <div>

        <h1>Happy Reading!</h1>
        <div v-for="blog in blogData">
            <p><RouterLink :to="{ name: 'DetailBlog', params: {itemId: blog.id}}">{{ blog.title }}</RouterLink></p>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import { RouterLink } from 'vue-router';

    export default {
        name: 'ListBlogs',
        data() {
            return {
                blogData: []
            }
        },
        async mounted() {
            const blogResponse = await axios.get('http://localhost:8000/api/items')
            this.blogData = blogResponse.data
        }

    }
</script>
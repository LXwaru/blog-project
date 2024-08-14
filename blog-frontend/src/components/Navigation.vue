<script>
import { RouterLink } from 'vue-router';
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'Navigation',
    computed: {
        ...mapGetters(['user'])
        }
    }

</script>


<template>
    <div v-if="user">
        <nav>
            <RouterLink to="/">Home</RouterLink>
            <hr>
            <RouterLink to="/ListBlogs">Read all blogs</RouterLink>
            <hr>
            <RouterLink to="/ListMyBlogs">View / Edit My Blogs</RouterLink>
            <hr>
            <RouterLink to="/CreateBlog">Write a New Blog</RouterLink>
            <hr>
            <RouterLink to="/ListUsers">See All Authors</RouterLink>
            <hr>
        </nav>
    </div>
    <div v-else>
        <nav>
            <RouterLink to="/">Home</RouterLink>
            <hr>
            <RouterLink to="/ListUsers">See All Authors</RouterLink>
            <hr>
        </nav>
    </div>

</template>

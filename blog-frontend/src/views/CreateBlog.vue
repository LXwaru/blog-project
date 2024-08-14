<template>
    <form @submit.prevent="postBlog">
        <input v-model="title" id="title" placeholder="title" />
        <textarea v-model="description" id="description" placeholder="your blog" rows="15" cols="50"></textarea>
        <button type="submit">Submit Blog</button>
    </form>
</template>

<script>
    import axios from 'axios'
    import { mapGetters } from 'vuex'
    
    export default {
        name: 'CreateBlog',
        computed: {
        ...mapGetters(['username', 'user'])
    },
        data() {
            return {
                title: "",
                description: "",
                userData: null,
                error: null,
                loading: false
            };
        },
        async mounted() {
            try {
                const token = localStorage.getItem('access_token');
                if (!token) {
                    throw new Error('no token found');
                }
                let userDataResponse = await axios.get('http://localhost:8000/users/me', {
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });
                this.userData = userDataResponse.data
            } catch (error) {
                console.error('Error creating blog', error)
                this.error = error.message;
            } finally {
                this.loading = false;
            }
        },
        methods: {
            async postBlog() {
                if (!this.title || !this.description || !this.userData) {
                    alert('Please fill out all the fields');
                    return;
                }
                const token = localStorage.getItem('access_token');
                if (!token) {
                    throw new Error('no token found');
                }
                const blogData = {
                    title: this.title,
                    description: this.description
                }
                console.log("blog created", blogData)
                alert("blog successfully created")
                this.$router.push('ListMyBlogs')
                try {
                    const blogCreate = await axios.post(`http://localhost:8000/api/users/${this.userData.id}/items/`, blogData, {
                        headers: {
                            'Authorization': `Bearer ${token}`,
                            'Content-Type': 'application/json'
                        }
                });
            } catch (error) {
                console.error('Error creating blog', error)
                alert('Failed to create blog. do something else')
            }
        }
    }
}
</script>
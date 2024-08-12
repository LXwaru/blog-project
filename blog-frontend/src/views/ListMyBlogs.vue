<template>
    <div>
        <h1>{{ username }}'s blogs</h1>
        <h3>View/Edit which blog?</h3>
        <div v-for="item in items">
            <ul>
                <li><RouterLink :to="{ name: 'DetailBlog', params: { itemId: item.id } }">{{ item.title }}</RouterLink></li>
            </ul>
        </div>
        <!-- Add a loading message or error message for better UX -->
        <div v-for="item in items">

        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router';
import { mapGetters, mapActions } from 'vuex'

export default {
    name: "ListMyBlogs",
    computed: {
        ...mapGetters(['username', 'user'])
    },
    data() {
        return {
            items: [],
            loading: true,
            error: null,
            userData: {}
        }
    },
    async mounted() {
        try{
            const token = localStorage.getItem('access_token');
            const userDataResponse = await axios.get('http://localhost:8000/users/me', {
                headers: {
                    'Authorization': `Bearer ${token}`
                }

            })
            
            this.userData = userDataResponse.data
            console.log(typeof this.userData.id)
            let itemResult = await axios.get(`http://localhost:8000/api/users/${this.user_id}/items`, {
                params: {
                    owner_id: this.userData.id
                }
            })
            this.items = itemResult.data
        } catch (error) {
            console.error('Error fetching items:', error);
            this.error = error.message;
        } finally {
            this.loading = false;
        }
        
    }
}
</script>
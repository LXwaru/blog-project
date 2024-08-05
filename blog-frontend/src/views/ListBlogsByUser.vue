<template>
    <div>
        <h1>{{user.username}}'s blogs</h1>
        <p  v-for="item in items" :key="item.id">
            <RouterLink :to="{ name: 'DetailBlog', params: { itemId: item.id } }">{{ item.title }}</RouterLink>    
        </p>

    </div>
</template>


<script>
import axios from "axios"

export default {
    name: "ListBlogsByUser",
    props: 
    {
        userId: {
            type: [Number, String], 
            required: true
        }
    },
    data() {
        return {
            items: [],
            user: {}

        }
    },
    async mounted() {
        const userId = Number(this.userId)
        if (isNaN(this.userId)) {
            throw new Error("invalid user ID")
        }
        let itemResults = await axios.get(`http://localhost:8000/api/users/${this.userId}/items/`, {
            params: {
                owner_id: userId
            },
        })
        let userResults = await axios.get(`http://localhost:8000/api/user/${this.userId}`, {
            params: {
                id: userId
            }
        })
            console.log(itemResults.data);
            console.log(userResults.data);
            this.items = itemResults.data;
            this.user = userResults.data;
    }
}
</script>

<style>


</style>
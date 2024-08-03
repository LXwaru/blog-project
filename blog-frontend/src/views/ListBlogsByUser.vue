<template>
    <div>
        <h1>{{userId}}'s blogs</h1>
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
            items: []

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
            }
        })
            console.log(itemResults.data);
            this.items = itemResults.data;
    }
}
</script>

<style>


</style>
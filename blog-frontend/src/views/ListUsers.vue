<template>
    <div>
        <h1>List of all Bloggers</h1>
        <p  v-for="user in users" :key="user.id">
            <RouterLink :to="{ name: 'listBlogsByUser', params: { userId: user.id } }">{{ user.username }}</RouterLink>    
        </p>

    </div>
</template>


<script>
import axios from "axios"
import { RouterLink } from "vue-router";

export default {
    name: "ListUsers",
    data() 
    {
        return {
            users:[],

        }
    },
    async mounted() 
    {   
        try {
            let userResult= await axios.get("http://localhost:8000/api/users/")
            console.log(userResult.data)
            this.users=userResult.data
        } catch (error) {
            console.error('Error fetching users:', error)
        }
    }
}
</script>

<style>
thead {
    text-transform: uppercase;

}

table {
    width: 700px;
}
td {
    color: orange;
    background-color: navy;
    border: double red 4px;
    text-align: center;
}


</style>
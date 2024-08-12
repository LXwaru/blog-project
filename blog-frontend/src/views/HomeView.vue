<template>
    <div v-if='user'>
        <h2>{{ this.user.username }}'s Homepage</h2>
        <ul>
            <li><RouterLink :to="{ name: 'ListMyBlogs', params: { userId: this.user.id } }">View or update my blogs</RouterLink></li>
            <li><RouterLink to="../ListUsers">Read blogs by select authors</RouterLink>   </li>  
            <li><RouterLink to="../CreateBlog">Write a new blog</RouterLink></li>     
        </ul>
    </div>
    <div v-else>
        <h2>Login to:</h2>
        <ul>
            <li>write/edit your own blog</li>
            <li>leave a comment on someone else's blog </li>
        </ul>
        <h2> Without an account, you can:</h2>
        <ul>
            <li>
                <RouterLink to="../ListUsers">Read blogs by select authors</RouterLink>
            </li>
        </ul>
    </div>
</template>


<script>
import axios from "axios"
import { RouterLink } from "vue-router";
import { mapGetters, mapActions } from 'vuex'

export default {
    name: "home",
    computed: {
        ...mapGetters(['username', 'user']),
        username() {
            return this.username
        }
    },
    data() 
    {
        return {
            accounts:[],
            items:[]
        }
    },
    async mounted() 
    {
        let accountResult = await axios.get("http://localhost:8000/api/users/")
        let itemResult = await axios.get(`http://localhost:8000/api/items/`)
        this.accounts=accountResult.data
        this.items=itemResult.data

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

.right-grid-item {
    grid-column: 2
}


</style>
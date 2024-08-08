<template>
    <Login />
    <div v-if='user'>
        <h1>Welcome Dear Reader</h1>
        <RouterLink to="../ListUsers">List of Authors</RouterLink>

    </div>
</template>


<script>
import axios from "axios"
import { RouterLink } from "vue-router";
import Login from '../components/Login.vue';

export default {
    name: "home",
    components: {
        Login
    },
    data() 
    {
        return {
            accounts:[],
            items:[],
            user: null

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
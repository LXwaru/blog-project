<template>
    <div>
        <h1>Welcome Dear Reader</h1>
        <RouterLink to="../ListUsers">List of Authors</RouterLink>

    </div>
</template>


<script>
import axios from "axios"
import { RouterLink } from "vue-router";

export default {
    name: "app",
    data() 
    {
        return {
            accounts:[],
            items:[],

        }
    },
    async mounted() 
    {
        let accountResult = await axios.get("http://localhost:8000/api/users/")
        let itemResult = await axios.get(`http://localhost:8000/api/items/`)
        console.log(accountResult.data)
        console.log(itemResult.data)

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
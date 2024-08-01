<template>
    <div class="right-grid-item">
        <table>
            <thead>
                <tr>
                    <td>username</td>
                    <td>active status</td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="account in accounts" :key="account.id">
                    <td>{{ account.username }}</td>
                    <td>{{ account.is_active }}</td>
                </tr>
            </tbody>
        </table>
        <table>
            <thead>
                <tr>
                    <td>author</td>
                    <td>title</td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in items" :key="item.id">
                    <td>{{ item.owner.username }}</td>
                    <td>{{ item.title }} -- {{ item.description }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>


<script>
import axios from "axios"

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
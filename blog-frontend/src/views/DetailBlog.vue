<template>
    <div>
        <h1>{{ item.title }}</h1>
        <p>{{ item.description }}</p>
    </div>
</template>

<script>
import axios from "axios"
export default {
    name: "BlogDetails",
    props: 
    {
        itemId: {
        type: [Number, String],
        required: true
        }
    },
    data() 
    {
        return {
            item: {}
        }
    },
    async mounted() 
    {
        const itemId = Number(this.itemId)
        if (isNaN(this.itemId)) {
            throw new Error("invalid blog ID")
        }
        let itemDetails = await axios.get(`http://localhost:8000/api/item/${this.itemId}`, {

            params: {
                item_id: itemId
            }
        }
        )
        this.item = itemDetails.data
        console.log(itemDetails.data)
    }
}
</script>
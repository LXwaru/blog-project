<template>
    <div>
        <h1>{{ item.title }}</h1>
        <p>{{ item.description }}</p>
        <Comment :blogId="blogId"/>
    </div>
</template>

<script>
import axios from "axios"
import Comment from "@/components/Comment.vue";

export default {
    name: "BlogDetails",
    components: {
        Comment
    },
    props: 
    {
        itemId: {
        type: [Number, String],
        required: true
        }
    },
    computed: {
        blogId() {
            return parseInt(this.$route.params.itemId, 10)
        }
    },
    data() {
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
    }
}
</script>
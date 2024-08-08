<template>
    <form>
        <input v-model="blogTitle" id="blogTitle" placeholder="title" />
        <input v-model="blogContent" id="blogContent" placeholder="your blog" />
    </form>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'CreateBlog',
        props: {
            userId: {
                type: [Number, String],
                required: true
            }
        },
        data() {
            return {
                blogTitle: "",
                blogContent: ""
            };
        },
        async mounted() {
            const userId = Number(this.userId)
            if (isNaN(this.userId)) {
                throw new Error("well, this isn't working right...")
            }
            let blogCreate = await axios.post(`http://localhost:8000/api/users/${this.userId}/items/`, {
                params: {
                    id: userId
                }
            });
        }
    }
</script>
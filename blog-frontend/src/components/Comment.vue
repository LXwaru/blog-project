<template>
    <div class="comment-component">
        <p>comments:</p>
        <div v-for="comment in this.comments">
            <p class="comment-box">{{ comment.content }} - {{ comment.commenter_username }}</p>
        </div>
        <div v-if="user">
            <textarea v-if="showInput" type="text" v-model="inputValue" placeholder="leave a comment" rows="5" cols="45"></textarea><br>
            <button v-if="showInput" @click="postComment">post comment</button>
            <button v-else @click="toggleInput">Leave a comment</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex';


export default {
    name: 'Comment',
    props: {
        blogId: {
            type: Number,
            required: true
        }
    },
    computed: {
        ...mapGetters(['user']),
        username() {
            return this.user?.username || ''
        }
    },
    data() {
            return {
                comments: [],
                userData: {},
                error: null,
                loading: false,
                showInput: false,
                inputValue: ''
            };
        },
    async mounted() {
        const commentResponse = await axios.get(`http://localhost:8000/api/${this.blogId}/comments`)
        this.comments = commentResponse.data
        if (this.user) {              
            try {
                const token = localStorage.getItem('access_token');
                let userDataResponse = await axios.get('http://localhost:8000/users/me', {
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }});
                this.userData = userDataResponse.data
            } catch (error) {
                console.error('there is no user logged in. you cannot leave a comment', error)
                this.error = error.message;
            } finally {
                this.loading = false
            }
    }
},
    methods: {
        toggleInput() {
                this.showInput = !this.showInput
        },
        async postComment() {
            if (!this.inputValue) {
                alert('must be at least 1 character');
                return;
            }
            const commentData = {
                content: this.inputValue,
            }
            try {
                const token = localStorage.getItem('access_token');
                await axios.post(`http://localhost:8000/api/${this.blogId}/${this.userData.username}/comment/`, commentData, {
                    headers: {
                        'Authorization': `Bearer ${token}`,
                        'Content-Type': 'application/json'
                    }
                });
                this.inputValue = '';
                this.toggleInput();
                window.location.reload();
            } catch (error) {
                console.error('error posting comment', error)
            }
        },
        async fetchComments() {
            try {
                const commentResponse = await axios.get(`http://localhost:8000/api/${this.blogId}/comments`)
                this.comments = commentResponse.data;
            } catch (error) {
                console.error('error fetching comments', error)
            }
        }
    }
}

</script>


<style>
.comment-component {
    padding: 15px;
    border: solid black .5px
}
.comment-box {
    padding-left: 5px;
    padding-right: 5px;
    border: solid black .5px;
}
</style>
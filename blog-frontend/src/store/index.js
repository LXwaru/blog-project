import { createStore } from 'vuex';


export default createStore({
    state: {
        username: '',
        userId: null,
        user: null
    },
    getters: {
        username: state => state.username,
        userId: state => state.userId,
        user: state => state.user
    },
    mutations: {
        SET_USER(state, payload) {
            state.username = payload.username;
            state.userId = payload.id;
            state.user = { username: payload.username, token: payload.token };
        },
        CLEAR_USER(state) {
            state.user = null;
            state.userId = null;
            state.username = '';
        }
    },
    actions: {
        loginUser({ commit }, { id, username, token }) {
            commit('SET_USER', { id, username, token });
            localStorage.setItem('access_token', token);
            localStorage.setItem('username', username);
            localStorage.setItem('userId', id);
        },
        logoutUser({ commit }) {
            commit('CLEAR_USER');
            localStorage.removeItem('access_token');
            localStorage.removeItem('username');
            localStorage.removeItem('userId');
        },
        async initializeUser({ commit }) {
            try {
                const token = localStorage.getItem('access_token');
                const username = localStorage.getItem('username');
                const userId = localStorage.getItem('userId');
                if (token && username && userId) {
                    commit('SET_USER', { username, id: userId, token });
                }
            } catch (error) {
                console.error('error initializing user:', error)
            }
        }
    }
});


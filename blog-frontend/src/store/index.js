import { createStore } from 'vuex';


export default createStore({
    state: {
        username: '',
        user: null
    },
    getters: {
        username: state => state.username,
        user: state => state.user
    },
    mutations: {
        SET_USER(state, payload) {
            state.username = payload.username;
            state.user = { username: payload.username, token: payload.token };
        },
        CLEAR_USER(state) {
            state.user = null;
            state.username = '';
        }
    },
    actions: {
        loginUser({ commit }, { username, token }) {
            commit('SET_USER', { username, token });
            localStorage.setItem('access_token', token);
            localStorage.setItem('username', username);
        },
        logoutUser({ commit }) {
            commit('CLEAR_USER');
            localStorage.removeItem('access_token');
            localStorage.removeItem('username');
        },
        initializeUser({ commit }) {
            const token = localStorage.getItem('access_token');
            const username = localStorage.getItem('username');
            if (token && username) {
                commit('SET_USER', { username, token });
            }
        }
    }
});


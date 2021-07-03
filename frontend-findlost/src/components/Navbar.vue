<template>
    <div class="navbar">
        <div class="navbar-logo">
            <router-link to="/" class="lost_found">Find my kind</router-link>
        </div>
        <div class="options-container">
            <div class="register-login" v-if="!isloggedin">
                <router-link to="/register">Register</router-link>
            </div>
            <div class="register-login" v-if="!isloggedin">
                <router-link to="/login">Login</router-link>
            </div>
            <div class="register-login" v-if="isloggedin">
                <div @click="logout">Logout</div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from "axios";
export default {
    name: "Navbar",
    data() {
        return {
            isloggedin: false,
        };
    },
    mounted() {
        axios.post("http://127.0.0.1:5000/isloggedin").then((res) => {
            var status = res["data"]["Status"];
            if (status == "TRUE") {
                this.isloggedin = true;
            }
        });
    },
    methods: {
        logout() {
            axios.post("http://127.0.0.1:5000/logout").then((res) => {
                var status = res["data"]["Status"];
                if (status == "Success") {
                    this.$router.push("/login");
                }
            });
        },
    },
};
</script>
<style scoped>
.navbar {
    background-color: transparent;
    width: 100%;
    display: flex;
    height: 12vh;
    justify-content: space-evenly;
    align-items: center;
    box-shadow: 0 8px 6px -6px black;
}
.navbar-logo {
    font-size: 3rem;
    font-family: "Montserrat";
    color: #232a31;
    /* font-weight: bold; */
}
.navbar-username {
    font-size: 1rem;
    font-family: "Montserrat";
    color: #232a31;
}

.options-container {
    height: 50%;
    width: 50%;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
}
.register-login {
    font-family: "Montserrat";
    font-size: 1rem;
    font-weight: 400;
    padding: 0.5rem;
    border: 1px solid #39a2db;
    border-radius: 0.5rem;
}
.register-login:hover {
    background-color: #39a2db;
    color: white;
    font-weight: 500;
    cursor: pointer;
}
a {
    text-decoration: none;
    color: #39a2db;
    border: 2px solid #39a2db;
    border-radius: 0.5rem;
}
a:hover {
    background-color: #39a2db;
    color: white;
}
</style>

<template>
    <div class="home">
        <Navbar />
        <div class="homebody">
            <div class="options-container">
                <router-link to="/lost" class="lost_found">Lost</router-link>
                <router-link to="/found" class="lost_found">Found</router-link>
            </div>
        </div>
    </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
export default {
    name: "Home",
    components: {
        Navbar,
    },
};
</script>
<style scoped>
.home {
    background-image: url("/bg1.jpeg");
}
.homebody {
    height: 88vh;
    /* background-color: white; */
    display: flex;
    justify-content: center;
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
    font-size: 1.5rem;
    font-weight: 400;
    padding: 1rem;
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
    color: white;
}
a:hover {
    background-color: #39a2db;
    color: white;
}
.lost_found {
    font-family: "Montserrat";
    font-size: 1.5rem;
    font-weight: 400;
    padding: 1rem;
    border: 1px solid white;
    border-radius: 0.5rem;
}
.lost_found:hover {
    background-color: #3277b4;
    color: white;
    font-weight: 500;
    cursor: pointer;
}
</style>

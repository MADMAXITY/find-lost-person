<template>
    <Navbar />
    <div class="homebody">
        <div class="options-container">
            <div class="lost_found">Lost</div>
            <div class="lost_found">Found</div>
        </div>
    </div>
</template>
<script>
import Navbar from "../components/Navbar.vue";
export default {
    name: "LostFound",
    components: {
        Navbar,
    },
};
</script>

<style scoped>
.homebody {
    height: 88vh;
    background-color: white;
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
.lost_found {
    font-family: "Montserrat";
    font-size: 1.5rem;
    font-weight: 400;
    padding: 1rem;
    border: 1px solid black;
    border-radius: 0.5rem;
}
.lost_found:hover {
    background-color: #3277b4;
    color: white;
    font-weight: 500;
    cursor: pointer;
}
</style>

<template>
    <div class="bodier">
        <Navbar />
        <div class="homebody">
            <div class="form-main">
                <label>Full Name</label>
                <input type="text" placeholder="Name" v-model="name" />
                <label>Email</label>
                <input type="email" placeholder="Email" v-model="email" />
                <label>Password</label>
                <input type="password" v-model="password" />
                <button @click="register">Submit</button>
            </div>
        </div>
    </div>
</template>
<script>
import Navbar from "../components/Navbar.vue";
import axios from "axios";
export default {
    name: "Register",
    data() {
        return {
            name: "",
            email: "",
            password: "",
        };
    },
    components: {
        Navbar,
    },
    methods: {
        register() {
            if (this.name == "" || this.email == "" || this.password == "") {
                alert("Invalid!");
            } else {
                var formdata = new FormData();
                formdata.append("Name", this.name);
                formdata.append("Email", this.email);
                formdata.append("Password", this.password);
                axios.post("/register", formdata).then((res) => {
                    var status = res["data"]["Status"];
                    if (status == "Success") {
                        alert("Success!");
                        this.$router.push("/login");
                    } else {
                        alert("Error!");
                    }
                });
            }
        },
    },
};
</script>
<style scoped>
.bodier {
    background-image: url("/bg3.jpeg");
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: 100% 100%;
}
.homebody {
    height: 88vh;
    /* background-color: white; */
    display: flex;
    justify-content: center;
    align-items: center;
}
.form-main {
    padding: 5rem;
    width: 20%;
    display: flex;
    flex-direction: column;
    align-items: center;

    background-color: #a2dbfa;
    border-radius: 1rem;

    box-shadow: 0 2.8px 2.2px rgba(0, 0, 0, 0.034),
        0 6.7px 5.3px rgba(0, 0, 0, 0.048), 0 12.5px 10px rgba(0, 0, 0, 0.06),
        0 22.3px 17.9px rgba(0, 0, 0, 0.072),
        0 41.8px 33.4px rgba(0, 0, 0, 0.086), 0 100px 80px rgba(0, 0, 0, 0.12);
}
label,
input {
    margin: 0.5rem;
}
label {
    font-size: 1.5rem;
    font-family: "Montserrat";
}
input {
    width: 100%;
    height: 2rem;
    padding: 0.1rem;
    outline: none;
    border: 1px solid #33658d;
    border-radius: 0.3rem;
}
button {
    margin-top: 0.5rem;
    padding: 0.5rem 1rem;
    background-color: white;
    outline: none;
    border: 1px solid #33658d;
}
button:hover {
    background-color: #33658d;
    color: white;
    cursor: pointer;
}
</style>

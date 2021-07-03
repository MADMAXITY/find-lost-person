<template>
    <div class="bodier">
        <Navbar />
        <div class="mainbody">
            <div class="formbody">
                <div class="label-mis">Enter Details of missing person</div>
                <input
                    type="text"
                    v-model="name"
                    class="details"
                    placeholder="Full Name"
                />
                <input
                    type="number"
                    v-model="phone"
                    class="details"
                    placeholder="Phone Number"
                />
                <input
                    type="number"
                    v-model="age"
                    class="details"
                    placeholder="Age"
                />
                <input
                    type="text"
                    v-model="gender"
                    class="details"
                    placeholder="Gender"
                />
                <input
                    type="number"
                    class="details"
                    placeholder="Road name,area, colony"
                />
                <input type="text" class="details" placeholder="City" />
                <input type="number" class="details" placeholder="Pincode   " />
                <input type="text" class="details" placeholder="District" />
                <input type="text" class="details" placeholder="State" />
                <input
                    type="number"
                    class="details"
                    placeholder="Weight(in Kg)"
                />
                <input
                    type="number"
                    class="details"
                    placeholder="Height(in foot)"
                />
                <textarea
                    placeholder="Other details of the person"
                    id=""
                    cols="10"
                    rows="5"
                ></textarea>

                <label for="img" class="imglabel">Select image:</label>
                <input
                    ref="fileInput"
                    type="file"
                    id="img"
                    name="img"
                    @input="pickFile"
                />

                <button @click="submitter">Submit</button>
            </div>
        </div>
    </div>
</template>
<script>
import axios from "axios";
import Navbar from "../components/Navbar.vue";
export default {
    name: "Lost",
    data() {
        return {
            name: "",
            phone: "",
            age: "",
            gender: "",
        };
    },
    components: {
        Navbar,
    },
    methods: {
        pickFile() {
            let input = this.$refs.fileInput;
            let file = input.files;
            console.log(file);
        },
        submitter() {
            let input = this.$refs.fileInput;
            let files = input.files;
            var formdata = new FormData();
            formdata.append("img", files[0]);
            formdata.append("name", this.name);
            formdata.append("phone", this.phone);
            formdata.append("age", this.age);
            formdata.append("gender", this.gender);

            axios.post("/api", formdata).then((res) => {
                console.log(res);
            });
            alert("Done");
            this.$router.push("/");
        },
    },
};
</script>
<style scoped>
.label-mis {
    font-family: "Montserrat";
    font-weight: 400;
    color: #b8dfd8;
    font-size: 1.5rem;
    border-bottom: 1px solid #b8dfd8;
}
.bodier {
    background-image: url("/bg2.jpeg");
}
.mainbody {
    height: 88vh;

    display: flex;
    justify-content: center;
    align-items: flex-start;
}
.formbody {
    margin-top: 1rem;
    min-height: 50vh;
    padding: 2rem;
    border-radius: 1rem;
    background-color: #4c4c6d;
    box-shadow: 0 2.8px 2.2px rgba(0, 0, 0, 0.034),
        0 6.7px 5.3px rgba(0, 0, 0, 0.048), 0 12.5px 10px rgba(0, 0, 0, 0.06),
        0 22.3px 17.9px rgba(0, 0, 0, 0.072),
        0 41.8px 33.4px rgba(0, 0, 0, 0.086), 0 100px 80px rgba(0, 0, 0, 0.12);
    display: flex;
    flex-direction: column;
}
.details {
    margin-top: 0.5rem;
    outline: none;
    border: none;
    padding: 0.3rem;
    font-family: "Montserrat";
    border-radius: 0.2rem;
}
textarea {
    margin-top: 0.5rem;
    outline: none;
    border: none;
    padding: 0.3rem;
    font-family: "Montserrat";
    border-radius: 0.2rem;
}
.imglabel {
    margin-top: 0.5rem;
    font-family: "Montserrat";
    color: white;
}
button {
    margin-top: 0.5rem;
    padding: 0.3rem;
    outline: none;
    font-family: "Montserrat";
    font-size: 1rem;
    background-color: white;
    border-radius: 0.3rem;
}
</style>

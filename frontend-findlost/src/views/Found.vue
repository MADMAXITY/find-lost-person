<template>
    <div class="bodier">
        <Navbar />
        <div class="homebody">
            <div class="formbody">
                <div class="label-mis">Enter Details of found person</div>

                <div class="detailtab">
                    <label for="img" class="imglabel">Select image:</label>
                    <input
                        ref="fileInput"
                        type="file"
                        id="img"
                        name="img"
                        class="imginput"
                        @input="pickFile"
                    />

                    <button @click="submitter">Submit</button>
                    <div class="label-wait" v-if="waitchecker">
                        Please Wait while the system is checking
                    </div>
                    <div class="founddata" v-if="found == true">
                        <div class="confirm">Person Found in database</div>
                        <div class="details">Name : {{ Name }}</div>
                        <div class="details">Phone : {{ Phone }}</div>
                        <div class="details">Age : {{ Age }}</div>
                        <div class="details">Gender : {{ Gender }}</div>
                    </div>
                    <div class="founddata" v-if="found == 'Not Found'">
                        <div class="confirm">Person not found in database</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import Navbar from "../components/Navbar.vue";
export default {
    name: "Found",
    data() {
        return {
            awaiting: false,
            found: false,
            Name: "",
            Phone: "",
            Age: "",
            Gender: "",
        };
    },
    components: {
        Navbar,
    },
    computed: {
        waitchecker() {
            return this.awaiting;
        },
    },
    methods: {
        pickFile() {
            let input = this.$refs.fileInput;
            let file = input.files;
            console.log(file);
        },
        submitter() {
            // alert("Awaiting result!");
            this.awaiting = true;
            let input = this.$refs.fileInput;
            let files = input.files;
            var formdata = new FormData();
            formdata.append("img", files[0]);

            axios.post("/found", formdata).then((res) => {
                console.log(
                    res["data"]["Status"],
                    res["data"]["Name"],
                    res["data"]["Phone"],
                    res["data"]["Age"],
                    res["data"]["Gender"]
                );
                if (res["data"]["Status"] == "Success") {
                    this.Name = res["data"]["Name"];
                    this.Phone = res["data"]["Phone"];
                    this.Age = res["data"]["Age"];
                    this.Gender = res["data"]["Gender"];
                    this.found = true;
                } else {
                    this.found = "Not Found";
                }
                this.awaiting = false;
            });
        },
    },
};
</script>
<style scoped>
.bodier {
    background-image: url("/bg2.jpeg");
}
.homebody {
    height: 88vh;
    /* background-color: white; */
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
.label-mis {
    font-family: "Montserrat";
    font-weight: 400;
    color: #b8dfd8;
    font-size: 1.5rem;
    border-bottom: 1px solid #b8dfd8;
}
.detailtab {
    margin-top: 4rem;
    height: 100%;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
}
.imglabel {
    margin-top: 0.5rem;
    font-family: "Montserrat";
    color: white;
}
.imginput {
    color: white;
    margin-top: 0.5rem;
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
.label-wait {
    font-size: 1.2rem;
    color: #ffe194;
}
.founddata {
    margin-top: 1rem;
}
.confirm {
    font-family: "Montserrat";
    font-size: 1.2rem;
    font-weight: 400;
    color: white;
}
.details {
    font-family: "Montserrat";
    font-size: 1.2rem;
    font-weight: 400;
    color: white;
}
</style>

from flask import Flask, redirect, url_for, request
from flask_wtf.csrf import CSRFProtect
import pandas as pd
from flask_cors import CORS
import time

csrf = CSRFProtect()

app = Flask(__name__)
CORS(app)

userdata = pd.read_csv("hasheddata.csv")
data = {
    "Email": list(userdata["Email"]),
    "Name": list(userdata["Name"]),
    "Password": list(userdata["Password"]),
}

user = None


@app.route("/success/<name>")
def success(name):
    return "welcome %s" % name


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["Email"]
        password = request.form["Password"]
        print(email, password)
        if (
            email in data["Email"]
            and password == data["Password"][data["Email"].index(email)]
        ):
            isloggedin = True
            user = email
            file = open("auth.txt", "w")
            file.write("True")
            file.close()
            return {"Status": "Success"}


@app.route("/logout", methods=["POST", "GET"])
def logout():
    file = open("auth.txt", "w")
    file.write("False")
    file.close()
    return {"Status": "Success"}


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        user = request.form["Name"]
        email = request.form["Email"]
        password = request.form["Password"]
        data["Name"].append(user)
        data["Email"].append(email)
        data["Password"].append(password)
        pd.DataFrame(data).to_csv("hasheddata.csv", index=False)
        print(user, email, password)

        print("here!")
    return {"Status": "Success"}


@app.route("/isloggedin", methods=["GET", "POST"])
def authcheck():
    file = open("auth.txt")

    if file.readline() != "False":
        file.close()
        return {"Status": "TRUE"}
    else:
        file.close()
        return {"Status": "FALSE"}


@app.route("/api", methods=["GET", "POST"])
@csrf.exempt
def imagegetter():
    print(request)
    if request.method == "POST":
        img = request.files["img"]
        name = request.form["name"]
        phone = request.form["phone"]
        age = request.form["age"]
        gender = request.form["gender"]
        img.save(f"Images/{name}.jpg")

        data = pd.read_csv("Data/lost.csv")
        data.loc[len(data)] = [name, phone, age, gender]
        data.to_csv("Data/lost.csv", index=False)

    return "Success"


@app.route("/found", methods=["GET", "POST"])
def found():
    time.sleep(3)
    if request.method == "POST":
        img = request.files["img"]
        name = " Shankar"
        data = pd.read_csv("Data/lost.csv")
        if name in list(data["Name"]):
            data = list(data.loc[list(data["Name"]).index(name)])
            return {
                "Status": "Success",
                "Name": str(data[0]),
                "Phone": str(data[1]),
                "Age": str(data[2]),
                "Gender": str(data[3]),
            }
        else:
            return {"Status": "Failed"}


if __name__ == "__main__":
    app.run(debug=True)

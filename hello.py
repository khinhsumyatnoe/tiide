from flask import Flask
app = Flask(_name_)

@app.route("/")
def khin():
    return "Hello world"
@app.route("/khin")
def tiide():
    return "Welcome to khinhsumyatnoe"

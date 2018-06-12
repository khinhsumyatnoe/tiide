from flask import Flask
app = Flask(__name__)

@app.route("/")
def khin():
return "Welcome to khinhsumyatnoe"

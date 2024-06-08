from flask import Flask, render_template, request, flash

app = Flask(__name__) # creates a class for our app

@app.route("/")
def index():
    return render_template("index.html")


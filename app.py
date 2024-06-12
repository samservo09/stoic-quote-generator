from flask import Flask, render_template, request, flash, redirect, url_for
import subprocess
import sys

app = Flask(__name__) # creates a class for our app
app.secret_key = 'syqcdtlejotfsldn'

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        # get the inputted data from the form
        gmail_acc = request.form['gmail_acc']
        send_time = request.form['send_time']
        str_duration = request.form['str_duration']
        
        python_interpreter = sys.executable
        
        # call the stoic.py script to process sending stoic emails
        subprocess.Popen([python_interpreter, 'stoic.py', gmail_acc, send_time, str_duration])
        
        # feedback to the user
        flash("You are now subscribed to receive daily stoic emails!", "Success!")
        
        # redirect user to avoid form resubmission
        return redirect(url_for('index'))

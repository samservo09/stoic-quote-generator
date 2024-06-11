from flask import Flask, render_template, request, flash
from stoic import set_sched, main

app = Flask(__name__) # creates a class for our app

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
        
        main()
        set_sched(gmail_acc, send_time, str_duration)

if __name__ == '__main__':
    app.run(debug=True)
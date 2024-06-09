from flask import Flask, render_template, request, flash
from datetime import datetime, timedelta
import threading
import time
from stoic import send_stoic_email

app = Flask(__name__) # creates a class for our app

@app.route("/")
def index():
    return render_template("index.html")

"""@app.route('/receive_email', methods=['POST'])
def receive_email():
    gmail_acc = request.form['gmail_acc']
    send_time = request.form['send_time']
    str_duration = int(request.form['str_duration'])
    
    # Calculate the end date for the email schedule
    end_date = datetime.now() + timedelta(days=str_duration)
    
    # Schedule email
    email_schedules.append((gmail_acc, send_time, end_date))
    
    return redirect(url_for('home'))

def email_scheduler():
    while True:
        now = datetime.now()
        for schedule in email_schedules:
            gmail_acc, send_time, end_date = schedule
            if now.strftime("%H:%M") == send_time and now < end_date:
                send_stoic_email(gmail_acc)
        time.sleep(60)  # Check every minute

# Start the email scheduler in a separate thread
scheduler_thread = threading.Thread(target=email_scheduler)
scheduler_thread.daemon = True
scheduler_thread.start()

if __name__ == '__main__':
    app.run(debug=True)"""
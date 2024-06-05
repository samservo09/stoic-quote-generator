
import requests
import json
import smtplib
import time
import schedule
from email.message import EmailMessage

# connect to an API and fetch a stoic quote
def fetch_quote():
    response = requests.get('https://stoic.tekloon.net/stoic-quote') #if 200, it is success
    if response.status_code == 200:
        stoic_data = response.text
        return json.loads(stoic_data)
    else:
        print("Failed to fetch quote. Status code: ", response)
        return None
    
# function to fetch a stoic quote
def email_stoic_quote():
    stoic_quote = fetch_quote()
    if stoic_quote:
    # convert the dictionary into a readable format
        author = stoic_quote.get('author')
        quote = stoic_quote.get('quote')
        body_content = f"{quote} - {author}"
    # send the email
    email_message("Hello! Here is your daily stoic message!", body_content, gmail_acc)

# function to send the email
def email_message(subject, body, to):
    msg = EmailMessage() # create message from the library
    msg.set_content(body) # call method 
    msg['subject'] = subject
    msg['to'] = to 
    
    # create variable for gmail user
    user = "stoic.msg.4u@gmail.com"
    msg['from'] = user
    password = "syqcdtlejotfsldn"
    
    # set server parameters
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo() # ensure connection is secure and no information leakage
    server.starttls() # enable encryption for the connection with TLS 
    server.login(user, password)
    server.send_message(msg)
    server.quit()

# main 
print("Do you want to receive emails about stoicism?")

gmail_acc = input("Enter your gmail account: ")
    
# closing
print("You are now subscribed to receive daily stoic quotes in your email!")

# set the schedule of sending
schedule.every().day.at("17:56").do(email_stoic_quote)

# keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

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
    
# fetch a stoic quote
stoic_quote = fetch_quote()

# convert the dictionary into a readable format
author = stoic_quote.get('author')
quote = stoic_quote.get('quote')
body_content = f"{quote} - {author}"

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
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

# function to send scheduled email
#def send_email_at(send_time):
    #time.sleep(send_time.timestamp() - #time.time())
  
print("Do you want to receive emails about stoicism?")

gmail_acc = input("Enter your gmail account: ")

#send_time = input("What frequency do you want to receive emails? \n[1] 1 Week \n[2]2 weeks \n[3]3 Weeks \n[4]1 Month:\n")

if __name__ == '__main__':
    email_message("Hello! Here is your daily stoic message!", body_content, gmail_acc)
    
# closing
print("You are now subscribed to receive daily stoic quotes in your email!")

# set the schedule of sending
schedule.every().day.at("19:15").do(email_message)

# keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

# connect to an API
import requests
import json
import smtplib
from email.message import EmailMessage

response_API = requests.get('https://stoic.tekloon.net/stoic-quote')
#print(response_API.status_code) #if 200, it is success

# get data from API
stoic_data = response_API.text 

# parse data into JSON format
parse_json = json.loads(stoic_data)

# convert the body dictionary into a string
body_content = f"{parse_json['quote']} - {parse_json['author']}"

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
    
print("Do you want to receive emails about stoicism?")

gmail_acc = input("Enter your gmail account: ")


if __name__ == '__main__':
    email_message("Hello! Here is your daily stoic message!", body_content, gmail_acc)
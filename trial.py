# connect to an API
import requests
import json
import smtplib
import random
from email.message import EmailMessage

response_API = requests.get('https://stoic.tekloon.net/stoic-quote')
#print(response_API.status_code) #if 200, it is success

# get data from API
stoic_data = response_API.text 

print(stoic_data)
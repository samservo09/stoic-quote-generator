
# connect to an API
import requests
import json

response_API = requests.get('https://stoic.tekloon.net/stoic-quote')
#print(response_API.status_code) #if 200, it is success

# get data from API


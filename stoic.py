
# connect to an API
import requests
import json

response_API = requests.get('https://stoic.tekloon.net/stoic-quote')
#print(response_API.status_code) #if 200, it is success

# get data from API
stoic_data = response_API.text 

# parse data into JSON format
parse_json = json.loads(stoic_data)

# extract data

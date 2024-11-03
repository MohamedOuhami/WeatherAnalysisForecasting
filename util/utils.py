# In this script, we will get the data from the API
import requests
import json
from dotenv import load_dotenv
import os
# Test fetching the data from the API

# Load the .env file
load_dotenv()

def authenticate():
    WEATHER_API_SECRET = os.environ.get("WEATHER_API_KEY")

def getData():
    
    authenticate()
    result = requests.get("http://api.weatherstack.com/current?access_key=eab271961a6cf4253bd8ecbf8e18e627&query=Casablanca")
    json_result = json.loads(result.text)
    pretty_result = json.dumps(json_result['current'],indent=2)
    

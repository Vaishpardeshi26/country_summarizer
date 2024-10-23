import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_url = 'https://api.api-ninjas.com/v1/country?name=India'
response = requests.get(api_url, headers={'X-Api-Key': 'TOvmq0lQPBV5rL9ldNmrzCps3wObbMtB9ZIg6dQu'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)

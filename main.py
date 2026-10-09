import os
import requests
from dotenv import load_dotenv

# This reads my .env file and makes the values available to python
load_dotenv()

app_id = os.getenv("APP_ID")
app_key = os.getenv("APP_KEY")

url = "https://api.adzuna.com/v1/api/jobs/us/search/1"

params = {
    "app_id": app_id,
    "app_key": app_key,
    "results_per_page": 10,
    "what": "data engineer",
    "where": "Columbus"
}

response = requests.get(url, params=params)


#API is going to return data as JSON, .json() converts it into a Python dictionary I can actually work with
data = response.json()

for job in data["results"]:
    print(job["title"], "-", job["company"]["display_name"])


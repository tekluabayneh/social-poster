import requests
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "LinkedIn-Version": "202306",   
    "Content-Type": "application/json"
}

def getUserId():
    res = requests.get("https://api.linkedin.com/v2/me", headers=headers)
    data = res.json()
    print("data from userid", data)
    return data

getUserId()

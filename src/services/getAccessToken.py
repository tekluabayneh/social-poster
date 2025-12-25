import requests 
import os 

URL = "https://www.linkedin.com/oauth/v2/accessToken"
CLIENT_ID = os.environ.get("LINKEDIN_CLIENT_ID")
CLIENT_SECRET = os.environ.get("LINKEDIN_CLIENT_SECRET")
params = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET
}


def GetAccessToken(): 
    res = requests.post(URL, params=params)
    data = res.json
    print(data)

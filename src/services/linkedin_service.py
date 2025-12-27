import requests
import os
from dotenv import load_dotenv 

load_dotenv()




ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")

POST_URL = "https://api.linkedin.com/rest/posts"

AUTHOR_URN = "urn:li:person:YOUR_PERSON_ID"
 
LINKEDINURL = os.environ.get("LINKEDINURL")

IMAGE_URN = f"urn:li:digitalmediaAsset:{LINKEDINURL}"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0",
    "LinkedIn-Version": "202306"
}

payload = {
    "author": AUTHOR_URN,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "Here’s my caption text for the image post!"
            },
            "shareMediaCategory": "IMAGE",
            "media": [
                {
                    "status": "READY",
                    "description": {
                        "text": "Optional description for the image"
                    },
                    "media": IMAGE_URN
                }
            ]
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}


def Post_Linkedin(message):
    response = requests.post(POST_URL, headers=headers, json=payload)
    print(response.status_code)
    print(response.json())



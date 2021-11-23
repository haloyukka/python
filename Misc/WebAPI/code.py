import requests
import os
import urllib
import json


bearer_token = os.environ.get("BEARER_TOKEN")
headers = {"Authorization": f"Bearer {bearer_token}"}
vr_academia = urllib.parse.quote('#VRアカデミア')
url = f'https://api.twitter.com/2/tweets/search/recent?query={vr_academia} -is:retweet'
response = requests.get(url, headers=headers)
json_response = response.json()
print(json.dumps(json_response, indent=2, ensure_ascii=False))
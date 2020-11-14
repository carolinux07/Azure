import requests
import os

account_id = os.environ["VIDEO_INDEXER_ACCOUNT"]
location = os.environ["VIDEO_INDEXER_LOCATION"]
api_key = os.environ["VIDEO_INDEXER_API_KEY"]
api_url = "https://api.videoindexer.ai"

headers = {"Ocp-Apim-Subscription-Key": api_key}

access_token_url = "{0}/auth/{1}/Accounts/{2}/AccessToken?allowEdit=true".format(api_url, location, account_id)
access_token_result = requests.get(access_token_url, headers=headers)
account_access_token = access_token_result.json()

video_id = "a059b4b246"

base_url = "{0}/{1}/Accounts/{2}".format(api_url, location, account_id)
video_index_url = "{0}/Videos/{1}/Index?accessToken={2}&language=English".format(
    base_url, video_id, account_access_token)

index_result = requests.get(video_index_url)

processing_state = index_result.json().get("state")
if processing_state != "Uploaded" and processing_state != "Processing":
    print("Full JSON:")
    print(index_result.json())
else:
    print("Video has not finished processing. Wait a minute then try again.")
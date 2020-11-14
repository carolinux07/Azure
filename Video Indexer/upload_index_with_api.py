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

# Video URL
# # video_url = "https://github.com/datakickstart/sample-content/blob/master/beach_waves_narrated.mp4?raw=true"
# video_name = "Beach waves"
# video_description = "Test video"

# form_data = None
# video_url_query_string = "&videoUrl={0}".format(video_url)

# Video local
video_path = "medias/vinheta2.mp4"
video_name = "vinheta2"
video_description = "Test video"

form_data = {'file': open(video_path, 'rb')}
video_url_query_string = ""

base_url = "{0}/{1}/Accounts/{2}".format(api_url, location, account_id)
video_upload_url = "{0}/Videos?accessToken={1}&name={2}&description={3}&privacy=private&partition=default{4}".format(
    base_url, account_access_token, video_name, video_description, video_url_query_string)
upload_result = requests.post(video_upload_url, files=form_data)

video_id = upload_result.json().get("id")
print("Uploaded Video ID: " + video_id)


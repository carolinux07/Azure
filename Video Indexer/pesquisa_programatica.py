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

search_query_string = "query=logo"
base_url = "{0}/{1}/Accounts/{2}".format(api_url, location, account_id)
search_url = "{0}/Videos/Search?accessToken={1}&{2}".format(
    base_url, account_access_token, search_query_string)

search_result = requests.get(search_url)

print("Search Results:")
print(search_result.json())

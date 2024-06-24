#This file contains a get and a post request for the Twitter API.
#After entering all credentials, the auth object is initialized using OAuth1
#Get Request is to get information of credential verification
#Post Request is posting message "Hello, Twitter API v2!"
import requests
from requests_oauthlib import OAuth1
import os

# Twitter API credentials
api_key = os.environ.get('API_KEY')
api_secret_key = os.environ.get('API_SECRET_KEY')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

# OAuth1 authentication object
auth = OAuth1(api_key, api_secret_key, access_token, access_token_secret)

#GET REQUEST - v1.1 authorization access
#API Endpoint for verifying credentials
get_url = "https://api.twitter.com/1.1/account/verify_credentials.json" 
get_response = requests.get(get_url, auth=auth) 
if get_response.status_code == 200:
    print("Get request successful!")
    data = get_response.json() 
    #converts json to a dict, data, to use info later
else:
    print("Get Request Unsuccessful!")


#POST REQUEST
post_url = "https://api.twitter.com/2/tweets"
post_message = {
    "text": "Hello, Twitter API v2!"
}
post_response = requests.post(post_url, auth=auth, json=post_message)
if post_response.status_code == 201:
    print("Post Request Successful!")
else:
    print(f"Failed to post, {post_response.status_code}")
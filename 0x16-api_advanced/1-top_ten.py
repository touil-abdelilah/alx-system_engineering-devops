#!/usr/bin/python3
"""Module for task 1"""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    
    # Define the URL for fetching the top 10 hot posts
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    # Make a GET request to the Reddit API
    response = requests.get(url, headers={"User-Agent": "My-User-Agent"}, allow_redirects=False)
    
    # Check if the response status code indicates success
    if response.status_code >= 300:
        print('None')
    else:
        # Extract and print the titles of the top 10 hot posts
        data = response.json().get("data", {}).get("children", [])
        for child in data:
            print(child.get("data", {}).get("title", "No title available"))

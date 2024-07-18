#!/usr/bin/python3
"""Module to query Reddit API and return number of subscribers"""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for the given subreddit. Returns 0 if the subreddit is invalid."""
    
    # Define the URL for the subreddit
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Make a GET request to the Reddit API
    response = requests.get(url, headers={"User-Agent": "My-User-Agent"}, allow_redirects=False)
    
    # Check if the request was successful and not redirected
    if response.status_code == 200:
        # Return the number of subscribers
        return response.json().get("data", {}).get("subscribers", 0)
    else:
        # Return 0 for invalid subreddit or other errors
        return 0

#!/usr/bin/python3
"""Module for task 0"""

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    # Send a GET request to the Reddit API for the subreddit information
    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    # If the response status code indicates an error (>= 300), return 0
    if sub_info.status_code >= 300:
        return 0

    # Extract and return the number of subscribers from the JSON response
    return sub_info.json().get("data").get("subscribers")

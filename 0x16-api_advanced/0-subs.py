#!/usr/bin/python3
"""Module for task 0"""

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    # Send a GET request to fetch information about the subreddit
    sub_info = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "My-User-Agent"},  # Include a custom User-Agent to avoid request issues
        allow_redirects=False  # Prevent automatic redirection
    )
    
    # Check if the request was successful or if there was an error
    if sub_info.status_code >= 300:
        return 0  # Return 0 if the subreddit is invalid or if there's an error

    # Return the number of subscribers from the response JSON
    return sub_info.json().get("data", {}).get("subscribers", 0)

#!/usr/bin/python3
"""Module for task 0"""

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    # Send GET request to Reddit API to fetch subreddit information
    sub_info = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},  # Custom User-Agent to avoid rate limits
                            allow_redirects=False)  # Do not follow redirects

    # Check if the response status code indicates an error or redirect
    if sub_info.status_code >= 300:
        return 0

    # Extract and return the number of subscribers from the JSON response
    return sub_info.json().get("data", {}).get("subscribers", 0)

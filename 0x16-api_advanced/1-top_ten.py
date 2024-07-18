#!/usr/bin/python3
"""Module for task 1"""

def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    
    import requests

    # Send a GET request to the Reddit API to fetch the top 10 hot posts for the given subreddit
    sub_info = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "My-User-Agent"},  # Include a custom User-Agent to avoid request issues
        allow_redirects=False  # Prevent automatic redirection to handle invalid subreddits
    )
    
    # Check if the response status code indicates an error or redirection
    if sub_info.status_code >= 300:
        print('None')  # Print 'None' if the subreddit is invalid or if there's an error
    else:
        # Extract and print the titles of the top 10 hot posts
        [print(child.get("data").get("title"))
         for child in sub_info.json().get("data").get("children")]

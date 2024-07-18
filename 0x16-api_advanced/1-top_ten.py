#!/usr/bin/python3
"""Module for task 1"""

def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import requests

    # Send a GET request to the Reddit API for the top 10 hot posts
    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    # If the response status code indicates an error (>= 300), print 'None'
    if sub_info.status_code >= 300:
        print('None')
    else:
        # Extract and print the titles of the top 10 hot posts
        [print(child.get("data").get("title"))
         for child in sub_info.json().get("data").get("children")]

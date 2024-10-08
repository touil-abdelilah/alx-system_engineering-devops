#!/usr/bin/python3
"""Module for querying the number of subscribers of a subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers. Returns 0 if the subreddit
        is not found or an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyApp/1.0"}  # Custom User-Agent to avoid issues

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            # Parse and return the number of subscribers
            return response.json().get("data", {}).get("subscribers", 0)
        else:
            # If the status code is not 200, return 0 (invalid subreddit)
            return 0
    except Exception:
        # In case of a network or parsing error, return 0
        return 0

#!/usr/bin/python3
"""Gathering data from an API"""


import requests
import time


def number_of_subscribers(subreddit):
    """for a given subreddit, returns the number of subscribers.
    If subreddit name doesn't exit, returns 0."""

    url = f'https://oauth.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        response_json = response.json()
        return (response_json['data']['subscribers'])

    elif response.status_code == 429:
        time.sleep(0.001)
        return number_of_subscribers(subreddit)
    else:
        return (0)

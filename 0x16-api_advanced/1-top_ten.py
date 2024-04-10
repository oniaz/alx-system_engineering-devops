#!/usr/bin/python3
"""Reddit API"""


import requests
import time


def top_ten(subreddit):
    """for a given subreddit, prints the titles of the first 10 hot posts."""

    limit = 10
    url = f'https://oauth.reddit.com/r/{subreddit}/hot.json?limit={limit}'
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        response_json = response.json()
        if len(response_json['data']['children']) < limit:
            limit = len(response_json['data']['children'])
        for i in range(limit):
            title = response_json['data']['children'][i]['data']['title']
            print(title)
    elif response.status_code == 429:
        time.sleep(0.001)
        return top_ten(subreddit)
    else:
        print("None")

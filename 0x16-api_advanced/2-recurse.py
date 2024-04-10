#!/usr/bin/python3
"""Reddit API"""


import requests
import time


def recurse(subreddit, hot_list=None, after=None):
    """for a given subreddit, returns a list titles of all of its hot articles.
    If there are no posts or the subreddit doesn't exist, returns None."""

    if hot_list is None:
        hot_list = []

    if after is not None:
        after = f"&after={after}"
    else:
        after = ""

    url = f'https://oauth.reddit.com/r/{subreddit}/hot.json?limit=100{after}'

    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        response_json = response.json()

        for i in range(len(response_json['data']['children'])):
            title = response_json['data']['children'][i]['data']['title']
            hot_list.append(title)

        if response_json['data']['after']:
            after = response_json['data']['children'][-1]['data']['name']
            return (recurse(subreddit, hot_list, after))
        else:
            return (hot_list)

    elif response.status_code == 429:
        time.sleep(0.001)
        return recurse(subreddit, hot_list, after)

    else:
        return (None)

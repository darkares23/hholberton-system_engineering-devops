#!/usr/bin/python3
"""
Function that queries the Reddit API and
returns the number of subscribers (not active users,
total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import json
from requests import get


def number_of_subscribers(subreddit):
    header = {'user-agent': 'X-Modhash'}
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    res = get(url, headers=header)
    resJson = res.json()
    if res.status_code == 404:
        return 0
    else:
        return resJson["data"]["subscribers"]

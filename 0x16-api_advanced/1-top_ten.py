#!/usr/bin/python3
"""
function that queries the Reddit API and
prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import json
from requests import get


def top_ten(subreddit):

    headers = {'user-agent': 'X-Modhash'}
    limit = {'limit': 10}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = get(url, headers=headers, allow_redirects=False, params=limit)
    resJson = res.json()
    if res.status_code == 404:
        print(None)
    else:
        for post in resJson["data"]["children"]:
            print(post["data"]["title"])

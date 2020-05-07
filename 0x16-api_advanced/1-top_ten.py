#!/usr/bin/python3
"""
function that queries the Reddit API and
prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import json
from requests import get
from pprint import pprint


def top_ten(subreddit):
    header = {'user-agent': 'X-Modhash'}
    limit = {'limit': 10}
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    res = get(url, headers=header, params=limit)
    resJson = res.json()
    subreditsList = resJson['data']['children']
    if res.status_code == 404:
        print('None')
    else:
        for subre in subreditsList:
            print(subre["data"]["title"])

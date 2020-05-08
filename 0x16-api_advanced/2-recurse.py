#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should
return None.
"""

import json
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    header = {'user-agent': 'X-Modhash'}
    params = {'after': after}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    res = get(url, headers=header, params=params, allow_redirects=False)
    resJson = res.json()
    if res.status_code == 404 or res.status_code == 301:
        return (None)
    else:
        for post in resJson["data"]["children"]:
            hot_list.append(post["data"]["title"])
        v_aft = resJson["data"]["after"]
        if v_aft is not None:
            return (recurse(subreddit, hot_list, v_aft))
        else:
            return hot_list

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
    limit = {'after': after}
    url = "https://reddit.com/r/{}/hot.json".format(
           subreddit)
    if after:
        limit['after'] = after
    res = get(url, headers=header, params=limit)
    resJson = res.json()
    if res.status_code == 404 or res.status_code == 302:
        return('None')
    else:
        for subs in resJson['data']['children']:
            hot_list.append(subs['data']['title'])
        after = res.json()['data']['after']
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)

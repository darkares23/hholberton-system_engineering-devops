#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should
return None.
"""

import json
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    header = {'user-agent': 'X-Modhash'}
    limit = {'limit': 100}
    url = "https://reddit.com/r/{}/hot.json?after{}".format(
           subreddit, str(after))
    if after:
        limit['after'] = after
    res = get(url, headers=header, params=limit)
    resJson = res.json()
    subreditsList = resJson['data']['children']
    if res.status_code == 404 or res.status_code == 302:
        print('None')
    else:
        for subs in subreditsList:
            hot_list.append(subs['data']['title'])
        after = res.json()['data']['after']
        if after is None:
            return recurse(subreddit, hot_list, after=resJson['data']['after'])
        else:
            return hot_list

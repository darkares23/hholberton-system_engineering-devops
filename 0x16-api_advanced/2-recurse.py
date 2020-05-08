#!/usr/bin/python3


import json
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    header = {'user-agent': 'X-Modhash'}
    limit = {'limit': 100}
    url = "https://reddit.com/r/{}/hot.json?after".format(subreddit)
    if after:
        limit['after'] = after
    res = get(url, headers=header, params=limit, allow_redirects=False)
    resJson = res.json()
    subreditsList = resJson['data']['children']
    if res.status_code == 404 or res.status_code == 302:
        print('None')
    else:
        for subs in subreditsList:
            hot_list.append(subs['data']['title'])
        if resJson['data']['after']:
            return recurse(subreddit, hot_list, after=resJson['data']['after'])
        else:
            return hot_list

#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress.
"""
import json
from requests import get
from sys import argv

if __name__ == "__main__":
    url1 = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    user = get(url1).json()
    user = user['username']
    tasks = get(url1 + '/todos').json()
    file = argv[1] + '.json'
    my_list = []
    _json = {}
    for task in tasks:
        _dict = {}
        _dict["task"] = task["title"]
        _dict["completed"] = task["completed"]
        _dict["username"] = user
        my_list.append(_dict)
    _json[argv[1]] = my_list
    with open(file, 'w') as f:
        json.dump(_json, f)

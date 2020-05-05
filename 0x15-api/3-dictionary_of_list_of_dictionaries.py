#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress.
"""
import json
from requests import get
from sys import argv

if __name__ == "__main__":
    file = 'todo_all_employees.json'
    url1 = 'https://jsonplaceholder.typicode.com/users'
    users = get(url1).json()
    _json = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        tasks = get(url1 + '/' + str(user_id) + '/todos').json()
        my_list = []
        for task in tasks:
            _dict = {}
            _dict["username"] = username
            _dict["task"] = task["title"]
            _dict["completed"] = task["completed"]
            my_list.append(_dict)
        _json[user_id] = my_list
    with open(file, 'w') as f:
        json.dump(_json, f)

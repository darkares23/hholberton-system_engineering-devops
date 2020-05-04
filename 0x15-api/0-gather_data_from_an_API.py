#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress.
"""
import requests
import json
from sys import argv


if __name__ == "__main__":
    id = argv[1]

    res = requests.get('https://jsonplaceholder.typicode.com/users?id={}'.
                       format(id))
    userText = json.loads(res.text)
    name = userText[0].get('name')

    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(id))
    todos = json.loads(todo.text)
    doneTitle = []

    for task in todos:
        if task['completed'] is True:
            doneTitle.append(task.get('title'))

    print ('Employee {} is done with task({}/{}):'.format(
           name, len(doneTitle), len(todos)))
    for task in doneTitle:
        print('\t {}'.format(task))

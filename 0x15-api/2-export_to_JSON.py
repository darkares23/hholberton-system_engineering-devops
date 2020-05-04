#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress.
"""
import requests
import json
import csv
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

    taskList = []
    dic = {'{}'.format(id): taskList}
    for i in todos:
        task = {}
        task['task'] = i.get('title')
        task['completed'] = i.get('completed')
        task['username'] = name
        taskList.append(task)

    with open("{}.json".format(id), 'w', encoding="utf-8") as f:
        f.write(json.dumps(dic))

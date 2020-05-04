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

    with open('{}.csv'.format(id), 'w', encoding="UTF-8") as f:
        tasks = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in todos:
            tasks.writerow(["{}".format(id),
                            "{}".format(name),
                            "{}".format(i.get('completed')),
                            "{}".format(i.get('title'))])

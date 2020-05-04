#!/usr/bin/python3
import json
import requests
from sys import argv


if __name__ == "__main__":
    _id = argv[1]

    res = requests.get('https://jsonplaceholder.typicode.com/users?id={}'.
                       format(_id))
    userText = json.loads(res.text)
    name = userText[0].get('name')

    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(_id))
    todos = json.loads(todo.text)
    doneTitle = []

    for task in todos:
        if task['completed'] is True:
            doneTitle.append(task.get('title'))

    print ('Employee {} is done with task({}/{}):'.format(
           name, len(doneTitle), len(todos)))
    for task in doneTitle:
        print('\t {}'.format(task))

#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress.
"""
import requests
import json
import csv

if __name__ == "__main__":

    res = requests.get('https://jsonplaceholder.typicode.com/users')
    usersText = json.loads(res.text)
    dic = {}
    for u in usersText:
        taskList = []
        dic[u.get('id')] = taskList
        todo = requests.get(
               'https://jsonplaceholder.typicode.com/todos?userId={}'
               .format(u.get('id')))
        todos = json.loads(todo.text)

        for i in todos:
            task = {}
            task['task'] = i.get('title')
            task['completed'] = i.get('completed')
            task['username'] = i.get('username')
            taskList.append(task)

    with open("todo_all_employees.json", 'w', encoding="utf-8") as f:
        f.write(json.dumps(dic))

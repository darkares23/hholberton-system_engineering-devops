#!/usr/bin/python3
import csv
from requests import get
from sys import argv

if __name__ == "__main__":
    url1 = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    user = get(url1).json()
    user = user['username']
    tasks = get(url1 + '/todos').json()
    _file = argv[1] + ".csv"
    with open(_file, 'w') as f:
        _writer = csv.writer(f, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL)
        for task in tasks:
            _writer.writerow([argv[1], user, task['completed'], task['title']])

#!/usr/bin/python3
""" export data in the CSV file """
import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    with requests.get(url) as res:
        name = res.json().get('username')

    with requests.get(url + '/todos') as res:
        todos = res.json()

    with open(f'{user_id}.json', 'w', encoding='utf-8') as json_file:

        # userId, id, title, completed
        tasks = [{'task': todo.get('title'), 'completed': todo.get(
            'completed'), 'username': name} for todo in todos]
        json.dump({user_id: tasks}, json_file)

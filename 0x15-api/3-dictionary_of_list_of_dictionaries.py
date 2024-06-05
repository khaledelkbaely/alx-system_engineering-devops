#!/usr/bin/python3
""" export data in the CSV file """
import json
import requests


if __name__ == '__main__':

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    users_dictionary = {}
    for user in users:
        user_id = user.get('id')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

        name = requests.get(url).json().get('username')

        todos = requests.get(url + '/todos').json()

        tasks = [{'username': name, 'task': todo.get('title'),
                  'completed': todo.get('completed')} for todo in todos]

        users_dictionary.update({f'{user_id}': tasks})

    with open('todo_all_employees.json', 'w', encoding='utf-8') as json_file:
        json.dump(users_dictionary, json_file)

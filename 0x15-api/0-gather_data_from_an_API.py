#!/usr/bin/python3
import requests
import sys


if __name__ == '__main__':
    user_id = int(sys.argv[1])
    if not isinstance(user_id, int):
        sys.exit()
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    with requests.get(url) as res:
        name = res.json().get('name')

    with requests.get(url + '/todos') as res:
        todo_list = res.json()
        completed = 0
        number_of_tasks = len(todo_list)
        todo_title_list = []
        for todo in todo_list:
            if todo.get('completed'):
                completed += 1
                todo_title_list.append(todo.get('title'))

    print('Employee {} is done with tasks({}/{}):'.
          format(name, completed, number_of_tasks))
    for title in todo_title_list:
        print('\t {}'.format(title))

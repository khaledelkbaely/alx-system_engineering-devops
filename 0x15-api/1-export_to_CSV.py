#!/usr/bin/python3
""" export data in the CSV file """
import csv
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    with requests.get(url) as res:
        name = res.json().get('username')

    with requests.get(url + '/todos') as res:
        todos = res.json()

    with open(f'{user_id}.csv', 'w', encoding='utf-8') as csv_file:
        csvwriter = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_ALL)

        for todo in todos:
            csvwriter.writerow([user_id, name, todo.get('completed'),
                                todo.get('title')])

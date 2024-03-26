#!/usr/bin/python3
"""Gathering data from an API"""


import csv
import requests
from sys import argv


def main(u_id):
    """for a given employee ID, rexport data in the CSV format about his/her
    TODO list."""
    user_url = f"https://jsonplaceholder.typicode.com/users?id={u_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={u_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    users = user_response.json()
    todos = todos_response.json()

    username = users[0]["username"]
    filename = f"{u_id}.csv"
    with open(filename, "w", encoding="utf-8") as file:
        writer = csv.writer(file)

        for todo in todos:
            row = f'"{u_id}","{username}","{todo["completed"]}","' +\
                    f'{todo["title"]}"\n'
            file.write(row)


if __name__ == "__main__":
    main(argv[1])

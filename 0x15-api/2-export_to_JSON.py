#!/usr/bin/python3
"""Gathering data from an API and exporting to a JSON file"""


import json
import requests
from sys import argv


def main(u_id):
    """for a given employee ID, exports data in JSON format about their
    TODO list."""

    user_url = f"https://jsonplaceholder.typicode.com/users?id={u_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={u_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    users = user_response.json()
    todos = todos_response.json()

    username = users[0]["username"]

    tasks = []

    for todo in todos:
        tasks_dic = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
            }

        tasks.append(tasks_dic)

    user_dict = {u_id: tasks}

    filename = f"{u_id}.json"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(user_dict))


if __name__ == "__main__":
    main(argv[1])

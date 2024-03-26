#!/usr/bin/python3
"""Gathering data from an API and exporting to a JSON file"""


import json
import requests
from sys import argv


def main():
    """retrieves and exports data for all employees to a JSON file"""

    users_url = f"https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users = users_response.json()

    users_info = {}

    for user in users:
        u_id = user['id']
        username = user['username']

        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={u_id}"
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        tasks = []

        for todo in todos:
            tasks_dic = {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": username
                }

            tasks.append(tasks_dic)

        users_info[u_id] = tasks

    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(users_info, file)
        # file.write(json.dumps(user_dict))


if __name__ == "__main__":
    main()

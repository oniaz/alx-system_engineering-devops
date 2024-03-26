#!/usr/bin/python3
"""Gathering data from an API"""


import csv
import requests
from sys import argv


def main(u_id):
    """for a given employee ID, export data in the CSV format about his/her
    TODO list."""
    user_url = f"https://jsonplaceholder.typicode.com/users?id={u_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={u_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    users = user_response.json()
    todos = todos_response.json()

    username = users[0]['username']

    # headers = ['id', 'size', 'x', 'y']
    # csv_writer = csv.DictWriter(file, fieldnames=headers)
    # csv_writer.writeheader()

    filename = f"{u_id}.csv"
    with open(filename, "w", encoding="utf-8") as file:

        writer = csv.writer(file)
        for todo in todos:
            row = [f"{u_id}", f"{username}", f"{todo['completed']}", f"{todo['title']}"]
            writer.writerow(row)

    # todos_c = len(todos)
    # done_todos = [todo for todo in todos if todo['completed']]
    # done_todos_c = len(done_todos)

    # print(f"Employee {name} is done with tasks({done_todos_c}/{todos_c}):")
    # for todo in done_todos:
    #     print(f"\t {todo['title']}")


if __name__ == "__main__":
    main(argv[1])

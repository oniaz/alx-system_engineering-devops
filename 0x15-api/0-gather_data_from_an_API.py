"""Gathering data from an API"""


import requests
from sys import argv


def main(Uid):
    """for a given employee ID, returns information about his/her TODO list."""
    user_url = f"https://jsonplaceholder.typicode.com/users?id={Uid}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={Uid}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    users = user_response.json()
    todos = todos_response.json()

    name = users[0]['name']
    todos_c = len(todos)
    done_todos = [todo for todo in todos if todo['completed']]
    done_todos_c = len(done_todos)

    print(f"Employee {name} is done with tasks({done_todos_c}/{todos_c}):")
    for todo in done_todos:
        print(f"\t {todo['title']}")


if __name__ == "__main__":
    main(argv[1])

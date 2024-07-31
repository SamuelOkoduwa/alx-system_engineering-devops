#!/usr/bin/python3
"""
This script uses the JSONPlaceholder API to gather data for a given employee ID.
It returns information about the employee's TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command line argument
    user_id = int(sys.argv[1])

    # URLs for the user and the user's TODO list
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    # Make a GET request to fetch user details
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Make a GET request to fetch user's TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Extract the employee's name from the user data
    employee_name = user_data.get('name')

    # Calculate the total number of tasks and the number of completed tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]

    # Print the employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


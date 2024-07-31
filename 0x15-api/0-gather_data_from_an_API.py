#!/usr/bin/python3
"""
This script uses the JSONPlaceholder API to gather data for a given employee ID
and returns information about the employee's TODO list progress.
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

    # Make GET requests to fetch user details and TODO list
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    # Extract employee name
    employee_name = user_data.get('name')

    # Calculate total and completed tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]

    # Print the employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks("
          f"{len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

#!/usr/bin/python3
"""
This script uses the JSONPlaceholder API to gather data for all employees
and exports the data in JSON format.
"""

import json
import requests

if __name__ == "__main__":
    # URL for users and todos
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Make GET requests to fetch users and todos
    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users_data = users_response.json()
    todos_data = todos_response.json()

    # Prepare data for JSON export
    data = {}
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')
        # Filter tasks by user ID and prepare the list of dictionaries
        user_tasks = [
            {
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            for task in todos_data if task.get('userId') == user_id
        ]
        # Store the tasks list under the user ID
        data[str(user_id)] = [{
            "username": username,
            "tasks": user_tasks
        }]

    # Write JSON data to file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file, indent=4)


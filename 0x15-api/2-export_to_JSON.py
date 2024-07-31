#!/usr/bin/python3
"""
This script uses the JSONPlaceholder API to gather data for a given employee ID
and exports the data in JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
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

    # Extract the username from the user data
    username = user_data.get('username')

    # Prepare data for JSON export
    data = {
        str(user_id): {
            username: [
                {
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                for task in todos_data
            ]
        }
    }

    # Write JSON data to file
    with open(f"{user_id}.json", 'w') as file:
        json.dump(data, file)

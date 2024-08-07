#!/usr/bin/python3
"""
This script uses the JSONPlaceholder API to gather data for a given employee ID
and exports the data in CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
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

    # Extract username from the user data
    username = user_data.get('username')

    # Write CSV data to file
    with open(f"{user_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                user_id,
                username,
                task.get('completed'),
                task.get('title')
            ])

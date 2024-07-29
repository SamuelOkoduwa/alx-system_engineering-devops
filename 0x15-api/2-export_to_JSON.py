#!/usr/bin/python3
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos?userId={employee_id}"
    
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)
    
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data from API.")
        sys.exit(1)
    
    user_data = user_response.json()
    todos_data = todos_response.json()
    
    employee_name = user_data.get("username")
    
    tasks = []
    for task in todos_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_name
        }
        tasks.append(task_dict)
    
    employee_tasks = {str(employee_id): tasks}
    
    with open(f"{employee_id}.json", mode='w') as json_file:
        json.dump(employee_tasks, json_file)


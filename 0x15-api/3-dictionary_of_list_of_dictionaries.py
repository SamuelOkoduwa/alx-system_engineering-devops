import json
import requests

def fetch_data():
    # Fetch user data
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users_response.json()

    # Fetch todo data
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos_response.json()

    # Prepare the data structure for JSON export
    all_tasks = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = []
        
        for todo in todos:
            if todo['userId'] == user_id:
                task_info = {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                user_tasks.append(task_info)
        
        all_tasks[user_id] = user_tasks

    # Export to JSON
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)

if __name__ == "__main__":
    fetch_data()


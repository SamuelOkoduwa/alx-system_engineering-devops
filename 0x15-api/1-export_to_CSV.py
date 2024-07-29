#!/usr/bin/python3
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
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
    
    with open(f"{employee_id}.csv", mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csv_writer.writerow([
                employee_id,
                employee_name,
                task.get("completed"),
                task.get("title")
            ])


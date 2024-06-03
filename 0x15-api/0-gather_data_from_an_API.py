#!/usr/bin/python3
"""
Gather employee data from API and display TODO list progress.
"""

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def get_employee_data(employee_id):
    user_url = f"{REST_API}/users/{employee_id}"
    todos_url = f"{REST_API}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_response.raise_for_status()
    todos_response.raise_for_status()

    return user_response.json(), todos_response.json()


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee, todos = get_employee_data(employee_id)
        emp_name = employee.get('name')

        completed_tasks = [task for task in todos if task.get('completed')]
        total_tasks = len(todos)
        number_of_done_tasks = len(completed_tasks)

        print(f"Employee {emp_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")

        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

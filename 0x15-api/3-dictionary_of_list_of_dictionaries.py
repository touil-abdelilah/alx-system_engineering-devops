#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    # Fetch all users from the API
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()

    # Fetch all TODO tasks from the API
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todoAll = {}

    # Iterate through each user to compile their TODO tasks
    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                # Create a dictionary for each task with its details
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        # Add the list of tasks for each user to the main dictionary
        todoAll[user.get('id')] = taskList

    # Write the compiled data to a JSON file
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)

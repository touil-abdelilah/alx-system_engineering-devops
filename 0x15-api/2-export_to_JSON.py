#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    # Get the user ID from command-line arguments
    userId = sys.argv[1]

    # Fetch user details from the API
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    # Fetch all TODO tasks from the API
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todoUser = {}
    taskList = []

    # Iterate through the TODO tasks and filter tasks for the specified user
    for task in todos:
        if task.get('userId') == int(userId):
            # Create a dictionary for each task with its details
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)

    # Store the tasks in a dictionary with the user ID as the key
    todoUser[userId] = taskList

    # Write the data to a JSON file with the user ID as the filename
    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)

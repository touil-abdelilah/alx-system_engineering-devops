#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

if __name__ == "__main__":

    # Get the employee ID from command-line arguments
    userId = sys.argv[1]

    # Fetch user details from the API
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    # Extract the user's name from the response
    name = user.json().get('name')

    # Fetch all TODO tasks from the API
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0

    # Count the total and completed tasks for the given user
    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    # Print the user's name and their task completion statistics
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    # Print the titles of completed tasks
    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))

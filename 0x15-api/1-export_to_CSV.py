#!/usr/bin/python3
"""Exports data in the CSV format"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    # Get the user ID from command-line arguments
    userId = sys.argv[1]

    # Fetch user details from the API
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    # Extract the username from the response
    name = user.json().get('username')

    # Fetch all TODO tasks from the API
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    # Create a CSV file with the user ID as the filename
    filename = userId + '.csv'
    with open(filename, mode='w') as f:
        # Initialize the CSV writer
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')

        # Write each task for the given user to the CSV file
        for task in todos.json():
            if task.get('userId') == int(userId):
                writer.writerow([userId, name, str(task.get('completed')),
                                 task.get('title')])

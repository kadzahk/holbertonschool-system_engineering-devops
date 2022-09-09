#!/usr/bin/python3
"""
Gather data from an API
"""
import csv
import requests
from sys import argv


class User:
    """Class User to create users from Json string"""

    def __init__(self, **kwargs):
        """Constructor method"""
        self.id = kwargs["id"]
        self.name = kwargs["name"]
        self.username = kwargs["username"]
        self.tasks = []

    def add_tasks(self, **allTasks):
        """Method to add tasks to list"""
        for task in allTasks.values():
            if task.userId == self.id:
                self.tasks.append(task)

    def tasksCompleted(self):
        """Method to print all complted tasks"""
        done = len([task for task in self.tasks if task.completed is True])
        print("Employee {} is done with tasks({}/{}):".format(self.name,
              done, len(((self.tasks)))))

        [print("\t {}".format(task.title))
         for task in self.tasks if task.completed is True]

    def exportToCsv(self):
        """Method to export all tasks as cvs"""

        with open("{}.csv".format(self.id), "w") as fd:
            writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
            for task in self.tasks:
                writer.writerow(
                    [task.userId,
                     self.username,
                     task.completed,
                     task.title]
                )


class Task:
    """Class to create Tasks from Json string"""

    def __init__(self, **kwargs):
        """Constructor Method"""
        self.userId = kwargs["userId"]
        self.id = kwargs["id"]
        self.title = kwargs["title"]
        self.completed = kwargs["completed"]


tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
users = requests.get("https://jsonplaceholder.typicode.com/users").json()
allUsers = {str(user["id"]): User(**user) for user in users}
allTasks = {str(task["id"]): Task(**task) for task in tasks}

if __name__ == "__main__":
    user = allUsers.get(argv[1])
    user.add_tasks(**allTasks)
    user.exportToCsv()

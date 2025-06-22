# task_manager.py -> to manage tasks, append and save it to a file, and mark it done

# import json module
import json
# import task from task.py
from task import Task

class TaskManager:
# def for constructor to initialize empty task list
    def __init__(self):
        self.tasklist = []
        
# def to load the file
    def load_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.tasklist = [Task.from_dict(task) for task in data]
        except FileNotFoundError:
            self.tasklist = []
              
# def to append given task to the list
    def add_task_to_list(self):
        self.tasklist.append(task)

# def to save it to a file
    def save_to_file(self, filename="tasks.json"):
        with open(filename, "r") as file:
            json.dump([task.to_dict() for task in self.tasklist], file)
  
# def to check the status of the tasks
# def to mark task as done
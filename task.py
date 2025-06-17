# task.py -> to handle the task input and to return it as object

# import datetime module
from datetime import datetime

class Task:
# constructor to initialize new object
    def __init__(self, taskname, deadline=None, category=None, priority="Normal", done=False):
        self.taskname = taskname
        self.deadline = deadline
        self.category = category
        self.priority = priority
        self.done = done
        
# to turn mark as done from false to true
    def to_mark_done(self):
        self.done = True
        
# def to return task list
# def to return task into object
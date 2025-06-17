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
        
# to turn task object into regular dictionary for easier saving of file (obj -> dict)
    def to_dict(self):
        return {
            "taskname" = self.taskname,
            "deadline" = self.deadline.strftime("%Y-%m-%d") if self.deadline else None,
            "category" = self.category,
            "priority" = self. priority,
            "done" = self.done
        }

# to return task into object (dict -> obj)
    @staticmethod
    def from_dict(data):
        deadline = datetime.strptime(data["deadline"], "%Y-%m-%d") if data["deadline"] else None
        return Task(data["taskname"], deadline, data["category", data["priority"], data{"done"}])
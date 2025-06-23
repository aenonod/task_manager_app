# timed_task.py -> to inherit task class and to add type and duration into the dict

# import task from task.py
from task import Task

class TimedTask(Task):
# def to initialize previous objects with additional info
    def __init__(self, taskname, deadline, category, priority, done=False, duration=0):
        super().__init__(taskname, deadline, category, priority, done)
        self.duration = duration
        
# def to return data into dict with additional info
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "TimedTask"
        data["duration"] = self.duration
        return data
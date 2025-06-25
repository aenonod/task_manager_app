# timed_task.py -> to inherit task class and to add type and duration into the dict

# import task from task.py
from task import Task
# import datetime module
from datetime import datetime

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
        if isinstance(self.deadline, datetime):
            data["deadline"] = self.deadline.strftime("%Y-%m-%d")
        return data

    @staticmethod
    def from_dict(data):
        deadline_str = data.get("deadline")
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d") if deadline_str else None
        return TimedTask(
            data["taskname"],
            deadline,
            data.get("category"),
            data.get("priority"),
            data.get("done", False),
            data.get("duration", 0)
        )
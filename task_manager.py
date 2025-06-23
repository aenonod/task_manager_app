# task_manager.py -> to manage tasks, append and save it to a file, and mark it done

# import json module
import json
# import task from task.py
from task import Task
# import timedtask from timed_task.py
from timed_task import TimedTask

class TaskManager:
# def for constructor to initialize empty task list
    def __init__(self):
        self.tasklist = []
        
# def to load the file
    def load_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.tasklist = [Task.from_dict(data) for d in data]
        except FileNotFoundError:
            self.tasklist = []
              
# def to append given task to the list
    def add_task_to_list(self, task):
        self.tasklist.append(task)

# def to save it to a file
    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasklist], file)
  
# def to check the tasks
    def list_of_task(self):
        for i, task in enumerate(self.tasklist):
            status = "✅" if task.done else "❌"
            print(f"[{status}] {i+1}. {task.taskname} - Priority: {task.priority}")
            
# def to mark task as done
    def mark_task_as_done(self, index):
        if 0 <= index < len(self.tasklist):
            self.tasklist[index].to_mark_done()
        else:
            print("Invalid task number. Please try again.")
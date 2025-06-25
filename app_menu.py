# app_menu.py -> contains the main menu of the app

# import datetime module
from datetime import datetime
# import task from task.py
from task import Task
# import task manager from task_manager.py
from task_manager import TaskManager
# import timedtask from timed_task.py
from timed_task import TimedTask

class AppMenu:
    def __init__(self):
        self.tm = TaskManager()
        self.tm.load_file()
        
# def to add task
    def add_task(self, taskname, deadline, category, priority, timed_task=False, duration=0):
        if timed_task:
            task = TimedTask(taskname, deadline, category, priority, False, duration)
        else:
            task = Task(taskname, deadline, category, priority)
        
        self.tm.add_task_to_list(task)
        self.tm.save_to_file()
        return f"'{taskname}' has been added successfully!"
        
# def to view tasks
    def view_task(self):
        return self.tm.list_of_task()

# def to mark task as done
    def mark_task(self, index):
        try:
            self.tm.mark_task_as_done(index)
            self.tm.save_to_file()
            return True, "Nice! Task marked as done!"
        except (ValueError, IndexError):
            return False, "Invalid input. Enter a valid number."
        
# def to meet the dev
    def meet_the_dev(self):
        return """
Abegail E. Nonod is a first-year Bachelor of Science in Computer Engineering student at the Polytechnic University of the Philippines - Main Campus. With a passion for organization and productivity, she chose to develop a task manager app as her final project in her Object-Oriented Programming course.

Abegail enjoys listing and organizing her tasks, which inspired her to create an app that reflects these habits. Her love for the color purple is clearly evident in the app's aesthetic. She's ready to learn more in order to improve this app.

Thank you for using Taskmate — Padayon!
"""
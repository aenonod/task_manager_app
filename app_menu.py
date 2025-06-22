# app_menu.py -> contains the main menu of the app

# import datetime module
from datetime import datetime
# import task from task.py
from task import Task
# import task manager from task_manager.py
from task_manager import TaskManager

class AppMenu:
# def to view the home menu (choices)
    def home(self):
        print("""===== TASKMATE =====
Press 1 to Add Task
Press 2 to View List of Tasks
Press 3 to Mark a Task Done
Press 4 to Exit""")
        choice = input("Choose an option: ")
        
# def to run the user choice
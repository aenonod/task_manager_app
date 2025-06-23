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
        self.tm.list_of_task()
        
# def to view the home menu (choices)
    def home(self):
        print("""
===== TASKMATE =====
[1] Add Task
[2] View List of Tasks
[3] Mark a Task Done
[4] Exit
""")
        
# def to run the user choice
    def run(self):
        while True:
            self.home()
            try:
                choice = int(input("Choose an option: "))
                
                if choice not in [1, 2, 3, 4]:
                    raise ValueError("Invalid input. Please enter a number between 1 and 4.")
                    continue
                
                if choice == 1:
                    taskname = input("Taskname: ").strip().title()
                    deadline_input = input("Deadline (YYYY-MM-DD / Optional): ").strip()
                    try:
                        deadline = datetime.strptime(deadline_input, "%Y-%m-%d") if deadline_input else None
                    except ValueError:
                        print("Invalid date format. Deadline will be ignored.")
                        deadline = None
                    category = input("Category (School/Work/Personal/Others): ").strip().capitalize()
                    priority = input("Priority (Low/Normal/Urgent): ").strip().capitalize()
                    if priority not in ["Low", "Normal", "Urgent"]:
                        print("Invalid priority input. Defaulting to Normal.")
                        priority = "Normal"
                        
                    timed_task = input("Is this a timed task (y/n): ").strip().lower()
                    if timed_task == "y":
                        try:
                            duration = int(input("Duration in hours: "))
                        except ValueError:
                            print("Invalid duration. Defaulting to 1 hour.")
                            duration = 1
                        task = TimedTask(taskname, deadline, category, priority, False, duration)
                    else:
                        task = Task(taskname, deadline, category, priority)
                    
                    self.tm.add_task_to_list(task)
                    self.tm.save_to_file()
                    print(f"'{taskname}' has been added successfully!")
                    
                elif choice == 2:
                    self.tm.list_of_task()
                    
                elif choice == 3:
                    try:
                        index = int(input("Input task number to mark as done: ")) - 1
                        self.tm.mark_task_as_done(index)
                        self.tm.save_to_file()
                        print("Nice! Task marked as done!")
                    except ValueError:
                        print("Invalid input. Enter a valid number.")
                        continue
                    
                elif choice == 4:
                    print("👋 Goodbye, user!")
                    break
                    
            except ValueError as error:
                print(f"Error: {error}")
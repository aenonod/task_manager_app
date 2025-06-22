# app_menu.py -> contains the main menu of the app

# import datetime module
from datetime import datetime
# import task from task.py
from task import Task
# import task manager from task_manager.py
from task_manager import TaskManager

tm = TaskManager()
tm.load_file()

class AppMenu:
# def to view the home menu (choices)
    def home(self):
        print("""===== TASKMATE =====
Press 1 to Add Task
Press 2 to View List of Tasks
Press 3 to Mark a Task Done
Press 4 to Exit""")
        
# def to run the user choice
    def run(self):
        while True:
            try:
                choice = int(input("Choose an option: "))
                
                if choice not in [1, 2, 3, 4]:
                    raise ValueError("Invalid input. Please try again.")
                
                if choice == "1":
                    taskname = input("Taskname: ")
                    deadline_input = input("Deadline (YYYY-MM-DD / Optional): ")
                    deadline = deadline.strftime(deadline_input, "%Y-%m-%d") if self.deadline_input else None
                    category = input("Category (School/Work/Personal/Others): ")
                    priority = input("Priority (Low/Normal/Urgent): ")
                    
                    task = Task(taskname, deadline, category, priority)
                    tm.add_task_to_list()
                    tm.save_to_file()
                elif choice == "2":
                    tm.list_of_task()
                elif choice == "3":
                    index = int(input("Input task number to mark as done: ")) - 1
                    tm.mark_task_as_done(index)
                    tm.save_to_file()
                    print("Nice! Task marked as done!")
                elif choice == "4":
                    print("👋 Goodbye, user!")
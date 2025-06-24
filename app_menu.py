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
        
# def to add task
    def add_task(self):
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
        
# def to view tasks
    def view_task(self):
        self.tm.list_of_task()

# def to mark task as done
    def mark_task(self):
        try:
            index = int(input("Input task number to mark as done: ")) - 1
            self.tm.mark_task_as_done(index)
            self.tm.save_to_file()
            print("Nice! Task marked as done!")
        except ValueError:
            print("Invalid input. Enter a valid number.")
        
# def to meet the dev
    def meet_the_dev(self):
        print("""
Abegail E. Nonod is a first-year Bachelor of Science in Computer Engineering student at the Polytechnic University
of the Philippines - Main Campus. With a passion for organization and productivity, she chose to develop a task
manager app as her final project in her Object-Oriented Programming course.

Abegail enjoys listing and organizing her tasks, which inspired her to create an app that reflects these habits.
Her love for the color purple is clearly evident in the app's aesthetic. More than just a project, Taskmate is her
way of contributing to the development of useful tools that can help not only students but users from all walks
of life.

Thank you for using Taskmate — Padayon!
""")
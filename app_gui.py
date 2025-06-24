# app_gui -> to turn text based app into gui

# import datetime module
from datetime import datetime
# import task from task.py
from task import Task
# import taskmanager from task_manager.py
from task_manager import TaskManager
# import timedtask from timed_task.py
from timed_task import TimedTask
# import appmenu from app_menu.py
from app_menu import AppMenu
# import tkinter
import tkinter as tk

task_manager = TaskManager()
task_manager.load_file()

# create a window
window = tk.Tk()
window.title("TASKMATE")
window.geometry("800x600")
icon = tk.PhotoImage(file='cool_logo.png')
window.iconphoto(True, icon)
window.config(background="#A095A7")

# create frame 1 for main menu
# sub welcome message: "What do you want to do?"
subwelcome_label = tk.Label(window,
                      text="What do you want to do?",
                      font=('Segoe UI', 15),
                      fg="#000000",
                      bg="#A095A7")
subwelcome_label.place(relx=0.5, y=160, anchor="center")
# welcome message: "Hello, Taskmate!"
welcome_label = tk.Label(window,
                      text="Hello, Taskmate!",
                      font=('Century Gothic', 40, 'bold', 'underline'),
                      fg="#000000",
                      bg="#A095A7")
welcome_label.place(relx=0.5, y=110, anchor="center")
# button 1: add task
menu = AppMenu()
add_task_button = tk.Button(window,
                      text="Add Task",
                      font=('Arial', 13),
                      fg="#000000",
                      bg="#E5DBF3",
                      padx=45,
                      pady=10)
add_task_button.config(command=menu.add_task)
add_task_button.place(relx=0.5, y=280,anchor="center")
# button 2: view task list
view_task_button = tk.Button(window,
                      text="View List of Tasks",
                      font=('Arial', 13),
                      fg="#000000",
                      bg="#E5DBF3",
                      padx=15,
                      pady=10)
view_task_button.config(command=menu.view_task)
view_task_button.place(relx=0.5, y=345,anchor="center")
# button 3: meet the dev
meet_dev_button = tk.Button(window,
                      text="Meet the Developer",
                      font=('Arial', 13),
                      fg="#000000",
                      bg="#E5DBF3",
                      padx=10,
                      pady=10)
meet_dev_button.config(command=menu.meet_the_dev)
meet_dev_button.place(relx=0.5, y=410,anchor="center")

window.mainloop()

# create frame 2 to add task
# create frame 3 for task list
# create frame 4 to meet the dev
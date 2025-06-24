# app_gui -> to turn text based app into gui

# import datetime module
from datetime import datetime
# import task from task.py
from task import Task
# import taskmanager from task_manager.py
from task_manager import TaskManager
# import timedtask from timed_task.py
from timed_task import TimedTask
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
subwelcome_label = tk.Label(window,
                      text="What do you want to do?",
                      font=('Segoe UI', 15),   # Courier New Segoe UI
                      fg="#000000",
                      bg="#A095A7")
subwelcome_label.place(relx=0.5, y=150, anchor="center")

welcome_label = tk.Label(window,
                      text="Hello, Taskmate!",
                      font=('Century Gothic', 40, 'bold', 'underline'),
                      fg="#000000",
                      bg="#A095A7")
welcome_label.place(relx=0.5, y=100, anchor="center")

window.mainloop()

# create frame 2 to add task
# create frame 3 for task list
# create frame 4 to meet the dev
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
window.geometry("400x400")
icon = tk.PhotoImage(file='cool_logo.png')
window.iconphoto(True, icon)
window.config(background="#A095A7")

window.mainloop()

# create frame 1 for main menu
# create frame 2 to add task
# create frame 3 for task list
# create frame 4 to meet the dev
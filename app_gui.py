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

# create a window
window = tk.Tk()
window.title("TASKMATE")
window.geometry("800x600")
icon = tk.PhotoImage(file='cool_logo.png')
window.iconphoto(True, icon)
window.config(background="#A095A7")

task_manager = TaskManager()
task_manager.load_file()

# create frames
main_frame = tk.Frame(window, bg="#A095A7")
add_task_frame = tk.Frame(window, bg="#A095A7")
view_task_frame = tk.Frame(window, bg="#A095A7")
meet_dev_frame = tk.Frame(window, bg="#A095A7")

for frame in (main_frame, add_task_frame, view_task_frame, meet_dev_frame):
    frame.place(relwidth=1, relheight=1)
    
# switch frames
def switch_frame(frame):
    frame.tkraise()

# create frame 1 for main menu
def render_main_menu():
    # sub welcome message: "What do you want to do?"
    subwelcome_label = tk.Label(main_frame, text="What do you want to do?",
                        font=('Segoe UI', 15),
                        fg="#000000", bg="#A095A7")
    subwelcome_label.place(relx=0.5, y=160, anchor="center")
    # welcome message: "Hello, Taskmate!"
    welcome_label = tk.Label(main_frame, text="Hello, Taskmate!",
                        font=('Century Gothic', 40, 'bold', 'underline'),
                        fg="#000000", bg="#A095A7")
    welcome_label.place(relx=0.5, y=110, anchor="center")
    # button 1: add task
    menu = AppMenu()
    add_task_button = tk.Button(main_frame, text="Add a Task", font=('Arial', 13),
                        fg="#000000", bg="#E5DBF3",
                        padx=45, pady=10)
    add_task_button.config(command=lambda: switch_frame(add_task_frame))
    add_task_button.place(relx=0.5, y=280,anchor="center")
    # button 2: view task list
    view_task_button = tk.Button(main_frame, text="View List of Tasks", font=('Arial', 13),
                        fg="#000000", bg="#E5DBF3",
                        padx=15, pady=10)
    view_task_button.config(command=lambda: switch_frame(view_task_frame))
    view_task_button.place(relx=0.5, y=345,anchor="center")
    # button 3: meet the dev
    meet_dev_button = tk.Button(main_frame, text="Meet the Developer", font=('Arial', 13),
                        fg="#000000", bg="#E5DBF3",
                        padx=10, pady=10)
    meet_dev_button.config(command=lambda: switch_frame(meet_dev_frame))
    meet_dev_button.place(relx=0.5, y=410,anchor="center")

render_main_menu()
switch_frame(main_frame)

# create frame 2 to add task
# create frame 3 for task list
# create frame 4 to meet the dev
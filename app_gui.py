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
window.geometry("600x600")
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
                        padx=40, pady=10)
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
def render_add_task():
    # message: "Add Your Task!"
    header_label = tk.Label(add_task_frame, text="Add Your Task! 📝",
                        font=('Century Gothic', 30),
                        fg="#000000", bg="#A095A7")
    header_label.place(relx=0.5, y=80, anchor="center")
    
    # message: "Taskname:"
    taskname_label = tk.Label(add_task_frame, text="Taskname:",
                        font=('Arial', 13),
                        fg="#000000", bg="#A095A7")
    taskname_label.place(relx=0.5, y=150, anchor="center")
    taskname_entry = tk.Entry(add_task_frame, font=('Arial', 13),
                        fg="#000000", bg="#E9D4F7")
    taskname_entry.place(relx=0.5, y=180, anchor="center")
    
    # message: "Deadline:"
    deadline_label = tk.Label(add_task_frame, text="Deadline (YYYY-MM-DD):",
                        font=('Arial', 13),
                        fg="#000000", bg="#A095A7")
    deadline_label.place(relx=0.5, y=220, anchor="center")
    deadline_entry = tk.Entry(add_task_frame, font=('Arial', 13),
                        fg="#000000", bg="#E9D4F7")
    deadline_entry.place(relx=0.5, y=250, anchor="center")
    
    # message: "Category:"
    category_label = tk.Label(add_task_frame, text="Category:",
                        font=('Arial', 13),
                        fg="#000000", bg="#A095A7")
    category_label.place(relx=0.5, y=290, anchor="center")
    category_options = ["Personal", "School", "Work", "Others"]
    category_var = tk.StringVar()
    category_var.set("Personal")
    category_menu = tk.OptionMenu(add_task_frame, category_var, *category_options)
    category_menu.config(font=('Arial', 13), bg="#E9D4F7", width=15)
    category_menu.place(relx=0.5, y=320, anchor="center")
    
    # message: "Priority:"
    priority_label = tk.Label(add_task_frame, text="Priority:",
                        font=('Arial', 13),
                        fg="#000000", bg="#A095A7")
    priority_label.place(relx=0.5, y=360, anchor="center")
    priority_options = ["Low", "Normal", "Urgent"]
    priority_var = tk.StringVar()
    priority_var.set("Normal")
    priority_menu = tk.OptionMenu(add_task_frame, priority_var, *priority_options)
    priority_menu.config(font=('Arial', 13), bg="#E9D4F7", width=15)
    priority_menu.place(relx=0.5, y=390, anchor="center")
    
render_add_task()
window.mainloop() 

# create frame 3 for task list
# create frame 4 to meet the dev
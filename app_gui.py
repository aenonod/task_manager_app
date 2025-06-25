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
from tkinter import messagebox

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
                        font=('Segoe UI', 15), fg="#000000", bg="#A095A7")
    subwelcome_label.place(relx=0.5, y=160, anchor="center")
    # welcome message: "Hello, Taskmate!"
    welcome_label = tk.Label(main_frame, text="Hello, Taskmate!",
                        font=('Century Gothic', 40, 'bold', 'underline'), fg="#000000", bg="#A095A7")
    welcome_label.place(relx=0.5, y=110, anchor="center")
    
    # button 1: add task
    menu = AppMenu()
    add_task_button = tk.Button(main_frame, text="Add a Task", font=('Arial', 13),
                        fg="#000000", bg="#E5DBF3", padx=40, pady=10)
    add_task_button.config(command=lambda: switch_frame(add_task_frame))
    add_task_button.place(relx=0.5, y=280,anchor="center")
    # button 2: view task list
    view_task_button = tk.Button(main_frame, text="View List of Tasks", font=('Arial', 13),
                        fg="#000000", bg="#E5DBF3", padx=15, pady=10)
    view_task_button.config(command=lambda: [render_view_task(), switch_frame(view_task_frame)])
    view_task_button.place(relx=0.5, y=345,anchor="center")
    # button 3: meet the dev
    meet_dev_button = tk.Button(main_frame, text="Meet the Developer", font=('Arial', 13),
                        fg="#000000", bg="#E5DBF3", padx=10, pady=10)
    meet_dev_button.config(command=lambda: switch_frame(meet_dev_frame))
    meet_dev_button.place(relx=0.5, y=410,anchor="center")

# create frame 2 to add task
def render_add_task():
    # message: "Add Your Task!"
    header_label = tk.Label(add_task_frame, text="Add Your Task! 📝",
                        font=('Century Gothic', 30), fg="#000000", bg="#A095A7")
    header_label.place(relx=0.5, y=70, anchor="center")
    
    # message: "Taskname:"
    taskname_label = tk.Label(add_task_frame, text="Taskname:",
                        font=('Arial', 13), fg="#000000", bg="#A095A7")
    taskname_label.place(relx=0.5, y=120, anchor="center")
    taskname_entry = tk.Entry(add_task_frame, font=('Arial', 13),
                        fg="#000000", bg="#E9D4F7")
    taskname_entry.place(relx=0.5, y=150, anchor="center")
    
    # message: "Deadline:"
    deadline_label = tk.Label(add_task_frame, text="Deadline (YYYY-MM-DD):",
                        font=('Arial', 13), fg="#000000", bg="#A095A7")
    deadline_label.place(relx=0.5, y=180, anchor="center")
    deadline_entry = tk.Entry(add_task_frame, font=('Arial', 13),
                        fg="#000000", bg="#E9D4F7")
    deadline_entry.place(relx=0.5, y=210, anchor="center")
    
    # message: "Category:"
    category_label = tk.Label(add_task_frame, text="Category:",
                        font=('Arial', 13), fg="#000000", bg="#A095A7")
    category_label.place(relx=0.5, y=240, anchor="center")
    category_options = ["Personal", "School", "Work", "Others"]
    category_var = tk.StringVar()
    category_var.set("Personal")
    category_menu = tk.OptionMenu(add_task_frame, category_var, *category_options)
    category_menu.config(font=('Arial', 13), bg="#E9D4F7", width=15)
    category_menu.place(relx=0.5, y=270, anchor="center")
    
    # message: "Priority:"
    priority_label = tk.Label(add_task_frame, text="Priority:",
                        font=('Arial', 13), fg="#000000", bg="#A095A7")
    priority_label.place(relx=0.5, y=300, anchor="center")
    priority_options = ["Low", "Normal", "Urgent"]
    priority_var = tk.StringVar()
    priority_var.set("Normal")
    priority_menu = tk.OptionMenu(add_task_frame, priority_var, *priority_options)
    priority_menu.config(font=('Arial', 13), bg="#E9D4F7", width=15)
    priority_menu.place(relx=0.5, y=330, anchor="center")
    
    # message: "Is this a timed task?"
    timed_label = tk.Label(add_task_frame, text="Is this a timed task?",
                        font=('Arial', 13), fg="#000000", bg="#A095A7")
    timed_label.place(relx=0.5, y=360, anchor="center")
    timed_var = tk.StringVar(value="No")
    timed_menu = tk.OptionMenu(add_task_frame, timed_var, "Yes", "No")
    timed_menu.config(font=('Arial', 13), bg="#E9D4F7", width=15)
    timed_menu.place(relx=0.5, y=390, anchor="center")

    # message: "Duration (in hours):"
    duration_label = tk.Label(add_task_frame, text="Duration (in hours):",
                            font=('Arial', 13), fg="#000000", bg="#A095A7")
    duration_entry = tk.Entry(add_task_frame, font=('Arial', 13),
                            fg="#000000", bg="#E9D4F7")

    # only show when "Yes" is selected
    def toggle_duration(*args):
        if timed_var.get() == "Yes":
            duration_label.place(relx=0.5, y=420, anchor="center")
            duration_entry.place(relx=0.5, y=450, anchor="center")
        else:
            duration_label.place_forget()
            duration_entry.place_forget()
    timed_var.trace_add("write", toggle_duration)
    
    # to submit task
    def submit_task():
        name = taskname_entry.get().strip().title()
        deadline_str = deadline_entry.get().strip()
        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d") if deadline_str else None
        except ValueError:
            messagebox.showerror("Invalid Input", "Deadline must be in YYYY-MM-DD format.")
            return
        category = category_var.get()
        priority = priority_var.get()

        if timed_var.get() == "Yes":
            try:
                duration = int(duration_entry.get())
                task = TimedTask(name, deadline, category, priority, False, duration)
            except ValueError:
                messagebox.showerror("Invalid Input", "Duration must be a number.")
                return
        else:
            task = Task(name, deadline, category, priority)
        task_manager.add_task_to_list(task)
        task_manager.save_to_file()
        messagebox.showinfo("Success", f"'{name}' has been added!")
        switch_frame(main_frame)

    submit_button = tk.Button(add_task_frame, text="Submit Task", font=('Arial', 13), bg="#E5DBF3",
                              command=submit_task)
    submit_button.place(relx=0.3, y=500, anchor="center")
    back_button = tk.Button(add_task_frame, text="Back", font=('Arial', 12), bg="#E5DBF3",
                            command=lambda: switch_frame(main_frame))
    back_button.place(relx=0.7, y=500, anchor="center")

# create frame 3 for task list
def render_view_task():
    for widget in view_task_frame.winfo_children():
        widget.destroy()

    header_label = tk.Label(view_task_frame, text="Your Task List",
                            font=('Century Gothic', 30), fg="#000000", bg="#A095A7")
    header_label.place(relx=0.5, y=70, anchor="center")

    # Scrollable canvas area
    task_canvas = tk.Canvas(view_task_frame, bg="#A095A7", highlightthickness=0)
    task_canvas.place(relx=0.05, rely=0.2, relwidth=0.85, relheight=0.6)

    scrollbar = tk.Scrollbar(view_task_frame, orient="vertical", command=task_canvas.yview)
    scrollbar.place(relx=0.9, rely=0.2, relheight=0.6)

    task_container = tk.Frame(task_canvas, bg="#A095A7")
    task_container.bind("<Configure>", lambda e: task_canvas.configure(scrollregion=task_canvas.bbox("all")))

    task_canvas.create_window((0, 0), window=task_container, anchor="nw")
    task_canvas.configure(yscrollcommand=scrollbar.set)

    # Store checkboxes and vars
    checkbox_vars = []

    for task in task_manager.tasklist:
        var = tk.BooleanVar(value=task.done)
        deadline_str = task.deadline.strftime("%Y-%m-%d") if task.deadline else "No deadline"
    # Check if TimedTask
        if isinstance(task, TimedTask):
            display_text = f"""{task.taskname} - {task.priority}  |  {task.category}  |  {deadline_str}  |  {task.duration} hrs"""
        else:
            display_text = f"""{task.taskname} - {task.priority}  |  {task.category}  |  {deadline_str}"""

        chk = tk.Checkbutton(task_container,
                            text=display_text,
                            variable=var,
                            bg="#A095A7",
                            font=('Arial', 12),
                            anchor="w")
        chk.pack(fill="x", padx=10, pady=5)
        checkbox_vars.append((task, var))

    # Apply button
    def apply_done_changes():
        for task, var in checkbox_vars:
            task.done = var.get()
        task_manager.save_to_file()
        tk.messagebox.showinfo("Saved", "Changes applied!")

    apply_button = tk.Button(view_task_frame, text="Apply Changes", font=('Arial', 13),
                             bg="#E5DBF3", command=apply_done_changes)
    apply_button.place(relx=0.3, y=500, anchor="center")
    back_button = tk.Button(view_task_frame, text="Back", font=('Arial', 12), bg="#E5DBF3",
                            command=lambda: switch_frame(main_frame))
    back_button.place(relx=0.7, y=500, anchor="center")

# create frame 4 to meet the dev

render_main_menu()
render_add_task()
render_view_task()
switch_frame(main_frame)
window.mainloop() 
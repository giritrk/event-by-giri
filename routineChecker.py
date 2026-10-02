import tkinter as tk
from tkinter import messagebox

def show_last_character(event):
    text = task_entry.get()

    if text:
        last_char_label.config(text="Last character: " + text[-1])
    else:
        last_char_label.config(text="Last character: None")

def routine_clicked(event):
    click_label.config(text="Routine area clicked!")

def check_task():
    task = task_entry.get().strip()

    if not task:
        messagebox.showwarning("Warning", "Please enter a task.")
    else:
        result_label.config(text="Next task: " + task)

# Create window
root = tk.Tk()
root.title("After-School Routine Checker")
root.geometry("400x350")

# Heading
title_label = tk.Label(
    root,
    text="After-School Routine",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

# Task entry
tk.Label(root, text="Enter your task:").pack()

task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=10)

# Display last character typed
last_char_label = tk.Label(root, text="Last character: None")
last_char_label.pack(pady=5)

# Bind keyboard event
task_entry.bind("<KeyRelease>", show_last_character)

# Routine area
routine_area = tk.Label(
    root,
    text="Click the Routine Area",
    bg="lightblue",
    width=30,
    height=3
)
routine_area.pack(pady=15)

# Bind mouse click
routine_area.bind("<Button-1>", routine_clicked)

click_label = tk.Label(root, text="")
click_label.pack()

# Check button
check_button = tk.Button(
    root,
    text="Check Routine",
    command=check_task
)
check_button.pack(pady=15)

# Next task
result_label = tk.Label(
    root,
    text="Next task will appear here.",
    font=("Arial", 12)
)
result_label.pack(pady=10)

root.mainloop()
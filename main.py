import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
import os

# Motivational Quotes
quotes = [
    "Believe you can and you're halfway there.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "You are stronger than you think.",
    "Do something today that your future self will thank you for.",
    "Every day is a new beginning."
]

# Timer functionality
def start_countdown():
    try:
        time_remaining = int(timer_entry.get()) * 60
        countdown(time_remaining)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def countdown(time_left):
    if time_left > 0:
        mins, secs = divmod(time_left, 60)
        timer_display.config(text=f"{mins:02d}:{secs:02d}")
        root.after(1000, countdown, time_left - 1)
    else:
        timer_display.config(text="Time's up!")
        messagebox.showinfo("Timer", "Time's up!")

# Notes functionality
def save_note():
    note_content = notes_text.get("1.0", "end-1c")
    with open("notes.txt", "w") as f:
        f.write(note_content)
    messagebox.showinfo("Save", "Note saved successfully!")

def load_note():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r") as f:
            notes_text.delete("1.0", "end")
            notes_text.insert("1.0", f.read())
    else:
        messagebox.showinfo("Load", "No saved notes found.")

# To-Do List functionality
def add_task():
    task = todo_entry.get()
    if task:
        todo_list.insert("end", task)
        todo_entry.delete(0, "end")

def delete_task():
    selected_task = todo_list.curselection()
    if selected_task:
        todo_list.delete(selected_task)

def mark_done():
    selected_task = todo_list.curselection()
    if selected_task:
        task = todo_list.get(selected_task)
        todo_list.delete(selected_task)
        todo_list.insert("end", f"{task} ✔")













































# To-Do List Tab
todo_tab = ttk.Frame(notebook)
notebook.add(todo_tab, text="To-Do List")

todo_entry = tk.Entry(todo_tab, font=("Times New Roman", 14))
todo_entry.pack(pady=10)

todo_buttons_frame = tk.Frame(todo_tab)
todo_buttons_frame.pack(pady=10)

tk.Button(todo_buttons_frame, text="Add", command=add_task).pack(side="left", padx=5)
tk.Button(todo_buttons_frame, text="Delete", command=delete_task).pack(side="left", padx=5)
tk.Button(todo_buttons_frame, text="Mark Done", command=mark_done).pack(side="left", padx=5)

todo_list = tk.Listbox(todo_tab, font=("Times New Roman", 12))
todo_list.pack(expand=1, fill="both", padx=10, pady=10)
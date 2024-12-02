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

# Calculator functionality
def calculate():
    try:
        result = eval(calc_entry.get())
        calc_entry.delete(0, "end")
        calc_entry.insert("end", str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid calculation.")

# Application Setup
root = tk.Tk()
root.title("Student Productivity Toolkit")
root.geometry("800x600")
root.configure(bg="#1e81b0")

notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both")

# Timer Tab
timer_tab = ttk.Frame(notebook)
notebook.add(timer_tab, text="Timer")

timer_entry = tk.Entry(timer_tab, font=("Times New Roman", 14))
timer_entry.pack(pady=10)

timer_display = tk.Label(timer_tab, text="00:00", font=("Times New Roman", 24))
timer_display.pack(pady=10)

timer_button = tk.Button(timer_tab, text="Start Countdown", command=start_countdown)
timer_button.pack()

# Notes Tab
notes_tab = ttk.Frame(notebook)
notebook.add(notes_tab, text="Notes")

notes_text = tk.Text(notes_tab, wrap="word", font=("Times New Roman", 12))
notes_text.pack(expand=1, fill="both", padx=10, pady=10)

notes_buttons_frame = tk.Frame(notes_tab)
notes_buttons_frame.pack(pady=10)

tk.Button(notes_buttons_frame, text="Save", command=save_note).pack(side="left", padx=5)
tk.Button(notes_buttons_frame, text="Load", command=load_note).pack(side="left", padx=5)

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

# Calculator Tab
calc_tab = ttk.Frame(notebook)
notebook.add(calc_tab, text="Calculator")

calc_entry = tk.Entry(calc_tab, font=("Times New Roman", 16), justify="right")
calc_entry.pack(fill="x", padx=10, pady=10)

calc_buttons_frame = tk.Frame(calc_tab)
calc_buttons_frame.pack()

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+"),
]

for row in buttons:
    row_frame = tk.Frame(calc_buttons_frame)
    row_frame.pack()
    for btn_text in row:
        btn = tk.Button(
            row_frame, text=btn_text, width=5, height=2,
            command=lambda t=btn_text: calculate() if t == "=" else calc_entry.insert("end", t) if t != "C" else calc_entry.delete(0, "end")
        )
        btn.pack(side="left", padx=2, pady=2)

# Quotes Tab
quotes_tab = ttk.Frame(notebook)
notebook.add(quotes_tab, text="Motivational Quotes")

quote_label = tk.Label(quotes_tab, text=random.choice(quotes), font=("Times New Roman", 16), wraplength=600, bg="#1e81b0", fg="#333")
quote_label.pack(pady=20)

tk.Button(quotes_tab, text="New Quote", command=lambda: quote_label.config(text=random.choice(quotes))).pack()

root.mainloop()

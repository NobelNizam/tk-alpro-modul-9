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



































# Calculator functionality
def calculate():
    try:
        result = eval(calc_entry.get())
        calc_entry.delete(0, "end")
        calc_entry.insert("end", str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid calculation.")
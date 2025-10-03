import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# -----------------
# Fun Scientist Calculator
# -----------------

def press(key):
    if key == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            show_joke(result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            scientist_label.config(text="😵 Oops! That didn’t work...")
    elif key == "C":
        entry.delete(0, tk.END)
        scientist_label.config(text="🧪 Ready for new numbers!")
    else:
        entry.insert(tk.END, key)

def show_joke(result):
    try:
        value = float(result)
    except:
        value = 0

    if value > 100000:
        scientist_label.config(text="🤯 Whoa! That's HUGE!")
    elif value < 0:
        scientist_label.config(text="😬 Negative vibes detected!")
    elif value == 42:
        scientist_label.config(text="🔬 Aha! The meaning of life!")
    else:
        jokes = [
            "😁 Numbers obey you!",
            "🧪 Science approves!",
            "🤓 Easy peasy lemon squeezy!",
            "🎉 Brilliant calculation!",
            "😎 You cracked it!"
        ]
        scientist_label.config(text=random.choice(jokes))

# -----------------
# Main Window
# -----------------
root = tk.Tk()
root.title("Fun Scientist Calculator")
root.config(bg="#cce6ff")  # light pastel blue
root.geometry("440x600")

# Entry field (bigger screen)
entry = tk.Entry(root, font=("Arial", 22), borderwidth=4, relief="ridge", justify="right

import tkinter as tk
from tkinter import messagebox
import math
import random

# --- Crazy Scientist Jokes ---
jokes = [
    "E=mc²... Easy = math calculator² 🤓",
    "That was so simple, my test tubes could solve it!",
    "Use your brain, not just buttons! 🧠",
    "I divided by zero once... the universe almost collapsed!",
    "Calculations complete... now where's my coffee? ☕",
    "Even Einstein would say: 'Nice job!'",
    "Math is just science in disguise! 🔬",
    "Oops, did I just invent time travel with that result?",
]

def scientist_speaks():
    joke = random.choice(jokes)
    messagebox.showinfo("Dr. Crazy Scientist says:", joke)

def press(num):
    entry.insert(tk.END, str(num))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        scientist_speaks()
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        messagebox.showerror("Dr. Crazy Scientist says:", "That formula is nonsense!")

def special(func):
    try:
        value = float(entry.get())
        if func == "sqrt":
            result = math.sqrt(value)
        elif func == "square":
            result = value**2
        elif func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        elif func == "log":
            result = math.log(value)
        else:
            result = value

        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        scientist_speaks()
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        messagebox.showerror("Dr. Crazy Scientist says:", "Your math broke my brain!")

# --- GUI Setup ---
root = tk.Tk()
root.title("Crazy Scientist Calculator")

entry = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=5)

# --- Buttons ---
buttons = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),("√",1,4),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),("x²",2,4),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),("sin",3,4),
    ("0",4,0),(".",4,1),("%",4,2),("+",4,3),("cos",4,4),
    ("C",5,0),("=",5,1),("tan",5,2),("log",5,3)
]

for (text,row,col) in buttons:
    if text in ["√","x²","sin","cos","tan","log"]:
        action = lambda t=text: special("sqrt" if t=="√" else 
                                        "square" if t=="x²" else 
                                        t)
    elif text == "C":
        action = clear
    elif text == "=":
        action = calculate
    else:
        action = lambda t=text: press(t)

    btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 12), command=action)
    btn.grid(row=row, column=col, padx=2, pady=2)

# --- Run app ---
root.mainloop()

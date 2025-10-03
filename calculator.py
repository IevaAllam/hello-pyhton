import tkinter as tk
from tkinter import messagebox
import math, random

# --- Crazy Scientist Jokes ---
jokes = [
    "E=mc²... Easy = math calculator² 🤓",
    "That was so simple, my test tubes could solve it!",
    "Even Einstein would say: 'Nice job!'",
    "I divided by zero once... the universe almost collapsed!",
    "Oops, did I just invent time travel with that result?",
    "Calculations complete... now where's my coffee? ☕",
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
root.configure(bg="#f6f6f6")

# Bigger display area
entry = tk.Entry(root, width=22, borderwidth=5, font=("Arial", 20, "bold"), 
                 bg="#ffffff", fg="#2f3640", relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=5, pady=15, ipady=10)

# --- Buttons (smaller + pastel colors) ---
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
        color = "#c8b6ff"  # pastel lavender
    elif text == "C":
        action = clear
        color = "#ffadad"  # pastel red
    elif text == "=":
        action = calculate
        color = "#a0e7e5"  # pastel teal
    elif text in ["/","*","-","+","%"]:
        action = lambda t=text: press(t)
        color = "#ffd6a5"  # pastel peach
    else:
        action = lambda t=text: press(t)
        color = "#bde0fe"  # pastel blue

    btn = tk.Button(root, text=text, width=5, height=2,
                    font=("Arial", 12, "bold"),
                    bg=color, fg="#2f3640",
                    relief="raised", bd=2)
    btn.config(command=action)
    btn.grid(row=row, column=col, padx=3, pady=3, ipadx=3, ipady=3)

# Reserve place for scientist character (we’ll add drawing/image here later)
char_label = tk.Label(root, text="🧑‍🔬", font=("Arial", 40), bg="#f6f6f6")
char_label.grid(row=1, column=5, rowspan=5, padx=15)

root.mainloop()

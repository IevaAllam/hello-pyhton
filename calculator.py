import tkinter as tk
from tkinter import messagebox
import math, random

# --- Crazy Scientist Jokes ---
jokes = [
    "Hmm... I was expecting E=mc², not that! 😅",
    "Oh no, I forgot my chalk again! 🧑‍🔬",
    "Even Einstein would need coffee for this... ☕",
    "That number looks dangerous... should I wear goggles? 👓",
    "My calculator is smarter than my assistant! 😂",
    "Oops... did I just discover a new law of physics?",
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
root.configure(bg="#d6f0ff")  # light blue background

# Bigger display area
entry = tk.Entry(root, width=16, borderwidth=5, font=("Comic Sans MS", 28, "bold"), 
                 bg="#ffffff", fg="#2f3640", relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10, ipady=15)

# Scientist character (near screen)
char_label = tk.Label(root, text="🧑‍🔬😢", font=("Arial", 36), bg="#d6f0ff")
char_label.grid(row=0, column=4, padx=10)

# --- Buttons (all white, grouped nicely) ---
buttons = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("%",4,2),("+",4,3),
    ("C",5,0),("=",5,1),("x²",5,2),("√",5,3),
    ("sin",6,0),("cos",6,1),("tan",6,2),("log",6,3),
]

for (text,row,col) in buttons:
    if text.isdigit():  # numbers → green
        fg_color = "#2ecc71"
    else:               # operators → dark grey
        fg_color = "#2f3640"

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

    btn = tk.Button(root, text=text, width=6, height=2,
                    font=("Comic Sans MS", 14, "bold"),
                    bg="#ffffff", fg=fg_color,
                    relief="raised", bd=3)
    btn.config(command=action)
    btn.grid(row=row, column=col, padx=5, pady=5, ipadx=3, ipady=3)

root.mainloop()

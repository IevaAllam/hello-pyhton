import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Main window
root = tk.Tk()
root.title("Crazy Scientist Calculator 🧪")
root.geometry("500x600")
root.config(bg="#b3e5fc")  # light blue lab background

# Screen (for input/output)
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=5, pady=20, padx=10, ipady=10)

# Scientist image
try:
    scientist_img = Image.open("scientist.png")  # put your happy scientist image here
    scientist_img = scientist_img.resize((140, 140))
    scientist = ImageTk.PhotoImage(scientist_img)
    label_scientist = tk.Label(root, image=scientist, bg="#b3e5fc")
    label_scientist.grid(row=0, column=5, rowspan=3, padx=10)
except:
    label_scientist = tk.Label(root, text="👨‍🔬", font=("Arial", 40), bg="#b3e5fc")
    label_scientist.grid(row=0, column=5, rowspan=3, padx=10)

# Button click function
def button_click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error!")
        messagebox.showerror("Error", "Oops! The scientist spilled the chemicals!")

# Button style
btn_style = {"font": ("Arial", 16), "bg": "white", "fg": "green", "width": 6, "height": 2}

# Buttons layout
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3), ("C",1,4),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3), ("^",2,4),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3), ("%",3,4),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3)
]

for (text, row, col) in buttons:
    if text == "=":
        action = calculate
    elif text == "C":
        action = clear
    else:
        action = lambda t=text: button_click(t)
    tk.Button(root, text=text, command=action, **btn_style).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()

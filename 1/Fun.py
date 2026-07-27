import tkinter as tk


def on_button_click(value):
    # Get the current value in the entry field
    current = entry.get()
    # Deletes everything 
    entry.delete(0, tk.END)
    # Inserts !
    entry.insert(0, current + str(value))

def on_equals():
    try:
        #i`m saving everythin in str, and that`s why eval is there
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
#Clear everything, later on to add the division by zero error and if something find out

def on_clear():
    entry.delete(0, tk.END)

def on_backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("340x580")



# Entry field
entry = tk.Entry(
    root, 
    font=("Arial", 20), 
    justify="right")

entry.grid(
    row=0,
    column=0, 
    columnspan=4, 
    padx=10, 
    pady=20, 
    ipady=10)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

#  number and operator buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(
            root,
            text=text,
            font=("Arial", 18),
            command=on_equals,
            bg="Green",
            fg="white"
        )
    else:
        btn = tk.Button(
            root,
            text=text,
            font=("Arial", 18),
            command=lambda value=text: on_button_click(value),
        )
    btn.grid(
        row=row,
        column=col,
        padx=5,
        pady=5,
        sticky="nsew",
        ipadx=20,
        ipady=20)


# Clear button
clear_btn = tk.Button(
    root,
    text="Clear",
    font=("Arial", 18),
    command=on_clear,
    bg="red",
    fg="white"  
)
clear_btn.grid(
    row=5,
    column=0,
    columnspan=2,
    padx=5,
    pady=5,
    sticky="nsew",
    ipadx=5,
    ipady=5
)
# Backspace button
backspace_btn = tk.Button(
    root,
    text="Delete",
    font=("Arial", 18),
    command=on_backspace,
    bg="orange",
    fg="white"
)
backspace_btn.grid(
    row=5,
    column=2,
    columnspan=2,
    padx=5,
    pady=5,
    sticky="nsew",
    ipadx=20,
    ipady=20
)



root.mainloop()

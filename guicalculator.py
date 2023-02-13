# Python-GUI-Calculator
#thmahir
import tkinter as tk

def calculate():
    first_number = int(first_number_entry.get())
    second_number = int(second_number_entry.get())
    operation = operation_var.get()

    if operation == "add":
        result = first_number + second_number
    elif operation == "subtract":
        result = first_number - second_number
    elif operation == "multiply":
        result = first_number * second_number
    elif operation == "divide":
        result = first_number / second_number
    
    result_label.config(text="Result: " + str(result))

root = tk.Tk()
root.title("T H MAHIR Calculator")

first_number_label = tk.Label(root, text="First Number")
first_number_label.grid(row=0, column=0)

first_number_entry = tk.Entry(root)
first_number_entry.grid(row=0, column=1)

second_number_label = tk.Label(root, text="Second Number")
second_number_label.grid(row=1, column=0)

second_number_entry = tk.Entry(root)
second_number_entry.grid(row=1, column=1)

operation_var = tk.StringVar(value="add")

add_button = tk.Radiobutton(root, text="Add", variable=operation_var, value="add")
add_button.grid(row=2, column=0)

subtract_button = tk.Radiobutton(root, text="Subtract", variable=operation_var, value="subtract")
subtract_button.grid(row=2, column=1)

multiply_button = tk.Radiobutton(root, text="Multiply", variable=operation_var, value="multiply")
multiply_button.grid(row=3, column=0)

divide_button = tk.Radiobutton(root, text="Divide", variable=operation_var, value="divide")
divide_button.grid(row=3, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=0, columnspan=2)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
#thmahir bio.link/thmahir

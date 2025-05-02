import math
import cmath
import tkinter as tk
from tkinter import messagebox
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x) if x >= 0 else cmath.sqrt(x)

def logarithm(x, base=math.e):
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    return math.factorial(x)

def complex_add(z1, z2):
    return z1 + z2

def complex_multiply(z1, z2):
    return z1 * z2

import sympy as sp

def evaluate_expression(expression):
    try:
        # Evaluate the expression using sympy for symbolic mathematics
        return sp.sympify(expression)
    except sp.SympifyError:
        return "Invalid expression"
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Scientific Calculator")
        self.expression = ""

        # Input field
        self.input_text = tk.StringVar()
        self.input_field = tk.Entry(root, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=30, insertwidth=4, width=14, borderwidth=4)
        self.input_field.grid(row=0, column=0, columnspan=4)

        # Creating buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', 'pow',
            '1', '2', '3', '-', 'log',
            '0', '.', '=', '+', 'C'
        ]

        row = 1
        col = 0
        for button in buttons:
            if button == '=':
                tk.Button(self.root, text=button, padx=20, pady=20, command=self.calculate).grid(row=row, column=col, columnspan=2, sticky=tk.W+tk.E)
                col += 2
            elif button == 'C':
                tk.Button(self.root, text=button, padx=20, pady=20, command=self.clear).grid(row=row, column=col)
                col += 1
            elif button in ['sqrt', 'pow', 'log']:
                tk.Button(self.root, text=button, padx=20, pady=20, command=lambda b=button: self.append_operator(b)).grid(row=row, column=col)
                col += 1
            else:
                tk.Button(self.root, text=button, padx=20, pady=20, command=lambda b=button: self.append_to_expression(b)).grid(row=row, column=col)
                col += 1

            if col > 4:
                col = 0
                row += 1

    def append_to_expression(self, char):
        self.expression += str(char)
        self.input_text.set(self.expression)

    def append_operator(self, operator):
        if operator == 'sqrt':
            self.expression += "sqrt("
        elif operator == 'pow':
            self.expression += "**"
        elif operator == 'log':
            self.expression += "log("
        self.input_text.set(self.expression)

    def calculate(self):
        try:
            # Use sympy to evaluate the expression
            result = evaluate_expression(self.expression)
            self.input_text.set(result)
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")

    def clear(self):
        self.expression = ""
        self.input_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

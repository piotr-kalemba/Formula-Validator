import tkinter as tk
from compute_formula import get_answer


root = tk.Tk()

root.title('Formula validator')

e = tk.Entry(root, width=45)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def add_to_entry(sign):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, current + sign)


def clear():
    e.delete(0, tk.END)


def show_answer():
    form = e.get()
    e.delete(0, tk.END)

    message = get_answer(form)
    e.insert(0, message)


p_button = tk.Button(root, text='p', padx=25, pady=10, command=lambda: add_to_entry('p'))
var_button = tk.Button(root, text='|', padx=25, pady=10, command=lambda: add_to_entry('|'))
left_button = tk.Button(root, text='(', padx=25, pady=10, command=lambda: add_to_entry('('))
right_button = tk.Button(root, text=')', padx=25, pady=10, command=lambda: add_to_entry(')'))

neg_button = tk.Button(root, text='~', padx=25, pady=10, command=lambda: add_to_entry('~'))
or_button = tk.Button(root, text='U', padx=25, pady=10, command=lambda: add_to_entry('U'))
and_button = tk.Button(root, text='&', padx=25, pady=10, command=lambda: add_to_entry('&'))
imp_button = tk.Button(root, text='=>', padx=25, pady=10, command=lambda: add_to_entry('=>'))
eqv_button = tk.Button(root, text='<=>', padx=25, pady=10, command=lambda: add_to_entry('<=>'))
clear_button = tk.Button(root, text='clear', padx=25, pady=10, command=clear)

validate_button = tk.Button(root, text='validate', padx=25, pady=10, command=show_answer)

p_button.grid(row=1, column=0)
var_button.grid(row=1, column=1)
left_button.grid(row=1, column=2)
right_button.grid(row=1, column=3)
neg_button.grid(row=2, column=0)
or_button.grid(row=2, column=1)
and_button.grid(row=2, column=2)
imp_button.grid(row=2, column=3)
eqv_button.grid(row=3, column=0)
clear_button.grid(row=3, column=1)
validate_button.grid(row=3, column=2, columnspan=2)

root.mainloop()
import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('240x230+150+150')
mainWindow['padx'] = 10

mainWindow.columnconfigure(0, weight=1, minsize=3)
mainWindow.columnconfigure(1, weight=1, minsize=3)
mainWindow.columnconfigure(2, weight=1, minsize=3)
mainWindow.columnconfigure(3, weight=1, minsize=3)
mainWindow.columnconfigure(4, weight=1000, minsize=3)
mainWindow.rowconfigure(0, weight=1, minsize=3)
mainWindow.rowconfigure(1, weight=1, minsize=3)
mainWindow.rowconfigure(2, weight=1, minsize=3)
mainWindow.rowconfigure(3, weight=1, minsize=3)
mainWindow.rowconfigure(4, weight=1, minsize=3)
mainWindow.rowconfigure(5, weight=1, minsize=3)
mainWindow.rowconfigure(6, weight=1000, minsize=3)

calculatorScreen = tk.Label(mainWindow)
calculatorScreen.grid(row=0, column=0, columnspan=4, sticky='ew')
calculatorScreen.config(border=2, relief='sunken')

# holds button values, row, column and span
buttons = [('C', 1, 0, 1), ('CE', 1, 1, 1),
           ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2, 1), ('+', 2, 3, 1),
           ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2, 1), ('-', 3, 3, 1),
           ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2, 1), ('*', 4, 3, 1),
           ('0', 5, 0, 1), ('=', 5, 1, 2), ('/', 5, 3, 1)]

import sys
print(sys.getsizeof(buttons))

for idx, button in enumerate(buttons):
    # name = f"button{idx+1}"
    value, x, y, span = button
    _button = tk.Button(mainWindow, width=3, height=1, text=value)
    _button.grid(row=x, column=y, columnspan=span, padx=1, pady=1, sticky='news')
    print(_button)

mainWindow.mainloop()
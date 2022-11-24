from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        a = 36
        b = 38
        value = float(x.get())
        print(value)
        if value <= a:
            meters.set(0)
        elif value >= b:
            meters.set(1)
        else:
            meters.set(float(abs(round(value-a/b-a, 2))))
    except ValueError:
        pass

root = Tk()
root.title("x to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

x = StringVar()
x_entry = ttk.Entry(mainframe, width=7, textvariable=x)
x_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="suhu").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

x_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
import tkinter as tk
from tkinter import ttk

# Defines the units in relation to meter for conversion, for example 1KM is 1000 meters.
units = {
    "meter": 1,
    "km": 1000,
    "cm": 0.01,
    "mm": 0.001,
    "mile": 1609.34,
    "feet": 0.3048,
    "inch": 0.0254,
    "yard": 0.9144
}


# Create root element
rootWindow = tk.Tk()
rootWindow.title("Units Converter")

# Create mainframe
frame = tk.Frame(rootWindow)
frame.grid(row=1, column=1, padx=10, pady=10, sticky="NESW")

# creating description label
label_entry = tk.Label(frame, text='Enter Value:')
label_entry.grid(row=1, column=1, columnspan=3, pady=10)

# Handlers


def to_convert(*args, **kwargs):
    value = float(from_value.get())
    from_units = units[from_unitsvar.get()]
    to_units = units[to_unitsvar.get()]
    to_units_label = to_unitsvar.get()
    converted = value * from_units / to_units
    to_value.set(f"{converted}")


def from_convert(*args, **kwargs):
    value = float(from_value.get())
    from_units = units[from_unitsvar.get()]
    to_units = units[to_unitsvar.get()]
    to_units_label = to_unitsvar.get()
    converted = value * from_units / to_units
    to_value.set(f"{converted}")


# creating left entry
from_value = tk.StringVar()
from_value.trace_variable("w", from_convert)
from_entry = tk.Entry(frame, textvariable=from_value)
from_entry.grid(row=2, column=1, columnspan=1, sticky="W,E")

# creating right entry
to_value = tk.StringVar()
to_value.trace_variable("w", to_convert)
to_entry = tk.Entry(frame, textvariable=to_value)
to_entry.grid(row=2, column=3, sticky="W,E")

# Creating left combobox
from_unitsvar = tk.StringVar()
from_units_box = ttk.Combobox(
    frame, textvariable=from_unitsvar, state="readonly")
from_units_box['values'] = tuple(units.keys())
from_units_box.current(0)
from_units_box.grid(row=3, column=1)

# creating right combobox
to_unitsvar = tk.StringVar()
to_units_box = ttk.Combobox(
    frame, textvariable=to_unitsvar, state="readonly")
to_units_box['values'] = tuple(units.keys())
to_units_box.current(0)
to_units_box.grid(row=3, column=3)


if __name__ == "__main__":
    rootWindow.mainloop()

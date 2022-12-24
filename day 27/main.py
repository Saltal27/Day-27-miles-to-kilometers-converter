from tkinter import *

window = Tk()
window.title("Miles to Kilometers converter")
window.minsize(width=300, height=300)
window.config(padx=75, pady=75)

miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

miles_unit = Label(text="Miles")
miles_unit.grid(column=2, row=0)
miles_unit.config(padx=25)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)
is_equal.config(padx=15, pady=25)

km_text = Label(text="0")
km_text.grid(column=1, row=1)
km_text.config(padx=15, pady=25)

km_unit = Label(text="Km")
km_unit.grid(column=2, row=1)
km_unit.config(padx=15, pady=25)


def convert():
    miles_value = float(miles_entry.get())
    km_value = round(miles_value * 1.609344, 2)
    km_text.config(text=km_value)


calculate = Button(text="calculate", command=convert)
calculate.grid(column=1, row=2)

window.mainloop()

from tkinter import *
from datetime import datetime
def age():
    year = int(year_entry.get())
    current_year = datetime.now().year
    result = current_year - year
    label_result.config(text="Age = " + str(result))
root = Tk()
root.title("Age Calculator")
root.geometry("300x200")
Label(root, text="Enter Birth Year").pack()
year_entry = Entry(root)
year_entry.pack()
Button(root, text="Calculate Age", command=age).pack()
label_result = Label(root, text="")
label_result.pack()
root.mainloop()

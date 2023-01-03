from tkinter import *

#Creating a new window and configurations
win = Tk()
win.title("Widget Examples")

#Labels
label = Label(text="Temperature")
label.grid (column=0, row=1)

label2 = Label(text="")
label2.grid (column=1, row=3)

#Entry
entry = Entry (width=30)
entry.grid (column=1, row=1)

def radio_used():
    x = int(entry.get())
    if radio_state.get() == 1:
        y = (x * 9)/5+32

    if radio_state.get() == 2:
        y = (x-32) * 5/9

    label2.config (text=f"THE CONVERTED TEMPERATURE IS {y}")

#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="C to F", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="F to C", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=2, row=1)
radiobutton2.grid(column=2, row=2)

mainloop()
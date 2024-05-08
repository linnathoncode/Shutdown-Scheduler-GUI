import tkinter as tk
from utils import submit, cancel
root = tk.Tk()

root.geometry("640x640")
root.title("Shutdown Scheduler")
label = tk.Label(root, text="Shutdown Scheduler", font=("arial", 20))
label.pack(padx=10, pady=10)

optionsHour = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24
]

optionsMinute= [
    0,
    5,
    10,
    15,
    20,
    25,
    30,
    35,
    40,
    45,
    50,
    55
]
clickedHour = tk.IntVar()
clickedHour.set(0)
clickedMinute = tk.IntVar()
clickedMinute.set(0)

def getter():
    shutdown = submit(clickedHour.get(), clickedMinute.get())
    clickedHour.set(0)
    clickedMinute.set(0)
menuFrame = tk.Frame(root)


dropdownHour = tk.OptionMenu(menuFrame, clickedHour, *optionsHour)
dropdownHour.grid(row=0, column=1)
hourLabel = tk.Label(menuFrame, text="Hour", font=("arial", 15)).grid(row=0, column=0,padx=10)

dropdownMinute = tk.OptionMenu(menuFrame, clickedMinute, *optionsMinute)
dropdownMinute.grid(row =1, column=1, padx=10)
minuteLabel = tk.Label(menuFrame, text="Minute", font=("arial", 15)).grid(row=1, column=0)

submitbtn = tk.Button(menuFrame, text="submit", command=getter,font=("arial", 15))
submitbtn.grid(row=2, column =1, pady=20, padx=10)

cancelbtn = tk.Button(menuFrame, text="cancel", command=cancel, font=("arial",15))
cancelbtn.grid(row=2, column =0)
menuFrame.pack(fill="y", pady= 150)

root.mainloop()


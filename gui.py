import tkinter as tk
from utils import submit, cancel, set_brightness
from customtkinter import *
root = CTk()

root.geometry("640x640")
root.title("Shutdown Scheduler")
label = CTkLabel(root, text="Shutdown Scheduler", font=("arial", 30))
label.pack(padx=10, pady=10)

#light or dark mode according to the system 
set_appearance_mode("System")
#set_default_color_theme("red.json")

optionsHour = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21',
    '22',
    '23',
    '24'
]

optionsMinute= [
    '0',
    '5',
    '10',
    '15',
    '20',
    '25',
    '30',
    '35',
    '40',
    '45',
    '50',
    '55'
]

testMenu = [
    "1",
    "2"
]

clickedHour = IntVar()
clickedHour.set(0)
clickedMinute = IntVar()
clickedMinute.set(0)

def submit_func():
    shutdown = submit(clickedHour.get(), clickedMinute.get())
    if shutdown > 0:
        set_brightness(0)
    clickedHour.set(0)
    clickedMinute.set(0)
def cancel_func():
    cancel()
    set_brightness(50)

menuFrame = CTkFrame(root)
dropdownHour = CTkOptionMenu(master=menuFrame,values=optionsHour, variable=clickedHour, font=("arial", 20))
dropdownHour.grid(row=0, column=1, pady=25)
hourLabel = CTkLabel(menuFrame, text="Hour", font=("arial", 20)).grid(row=0, column=0,sticky="e")

dropdownMinute = CTkOptionMenu(master=menuFrame,values=optionsMinute, variable=clickedMinute, font=("arial", 20))
dropdownMinute.grid(row=1, column=1)
minuteLabel = CTkLabel(menuFrame, text="Minute", font=("arial", 20)).grid(row=1, column=0,sticky="e")

submitbtn = CTkButton(menuFrame, text="submit", command=submit_func, font=("arial", 30))
submitbtn.grid(row=2, column =1, pady=25, padx=50)

cancelbtn = CTkButton(menuFrame, text="cancel", command=cancel_func, font=("arial", 30),hover_color="red")
cancelbtn.grid(row=2, column =0,pady=25, padx=50)
menuFrame.pack(pady= 150)

root.mainloop()


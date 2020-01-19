import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
import os
import api2
from PIL import Image, ImageTk


root = tk.Tk()


def addApp():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))


def openUI():
    canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
    canvas.pack()

    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    openFile = tk.Button(root, text="Open File",
                         padx=10, pady=5, fg="white", bg='#263D42', command=addApp)

    openFile.pack()

    runApps = tk.Button(root, text="Sort", padx=10,
                        pady=5, fg="white", bg='#263D42')

    runApps.pack()
    filename = filedialog.askopenfilename()
    print(filename)
    from api2 import getImageInfo
    info = getImageInfo(filename)
    print(info)
    x = info
    # print(x)
    compost = Image.open(
        "C:\\Users\\hamad\\Downloads\\API Project\\assets\\compost.jpg")
    plastic = Image.open(
        "C:\\Users\\hamad\\Downloads\\API Project\\assets\\paper-bin.jpg")
    recycle = Image.open(
        "C:\\Users\\hamad\\Downloads\\API Project\\assets\\recycling-bin.jpg")

    for label in x:
        if label.lower() in ["peel", "food", "fruit"]:
            render = ImageTk.PhotoImage(compost)
            img = Label(image=render)
            img.image = render
            img.place(x=0, y=0)
            break
        elif label.lower() in ["paper", "napkins", "cardboard"]:
            render = ImageTk.PhotoImage(recycle)
            img = Label(image=render)
            img.image = render
            img.place(x=0, y=0)
            break
        elif label.lower() in ["plastic", "bottle"]:
            render = ImageTk.PhotoImage(plastic)
            img = Label(image=render)
            img.image = render
            img.place(x=0, y=0)
            break

    root.mainloop()


openUI()

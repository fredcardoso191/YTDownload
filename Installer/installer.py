import shutil
import pathlib
import isempty as emp
import language_os as los
import shortcut
import sys
import layout
from tkinter import messagebox
from tkinter import *

getpath = str(pathlib.Path().resolve()) + "\Youtube Download"

source = getpath.replace('\\', '/')

def install(folder_path):
    if emp.isEmpty(folder_path):
        messagebox.showwarning(los.title(), los.pathinvalid())
    else:
        destination = folder_path + "/Youtube Download"
        dest = shutil.copytree(source, destination)
        shortcut.create(folder_path)

        window = Tk()
        window.resizable(width=False, height=False)
        window.iconbitmap('icon.ico')
        window.title("Setup - Youtube Download")

        width = 600
        height = 400

        width_screen = window.winfo_screenwidth()
        height_screen = window.winfo_screenheight()

        posx = width_screen/2 - width/2
        posy = height_screen/3 - height/3

        window.geometry("%dx%d+%d+%d" % (width, height, posx, posy))

        lbFinish = Label(window, text=los.installfinish(), font=("Arial", 15))
        lbFinish.place(x=150, y=40)

        btnButton = layout.HoverButton(window, text=los.finishbutton(), activebackground='#fcf5ff', width=15, command=sys.exit)
        btnButton.place(x=480, y=370)

        window.mainloop()
        sys.exit(0)
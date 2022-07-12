import getpass
import pathlib
from tkinter import *
from tkinter import filedialog as fd
import language_os as los
import installer as i
import sys
import layout

drive = pathlib.Path.home().drive
user = getpass.getuser()

def browseFiles():
    folder_path = fd.askdirectory(initialdir= "/", title=los.finish())
    if folder_path is None:
        folder_path = ""
    else:
        setPath(folder_path)

def setPath(folder_path):
    enPath = Entry(root, font=("Arial", 12), width=30)
    enPath.place(x=80, y=50, height=26)
    enPath.insert(3, folder_path)
    enPath.configure(state='disabled')

    btnInstall = layout.HoverButton(root, text=los.install(), activebackground='#fcf5ff', width=12, height=1, command=lambda:[i.install(folder_path)])
    btnInstall.place(x=400, y=370)

root = Tk()
root.resizable(width=False, height=False)
root.iconbitmap("icon.ico")
root.title("Setup - Youtube Download")

width = 600
height = 400

width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()

posx = width_screen/2 - width/2
posy = height_screen/2 - height/2

root.geometry("%dx%d+%d+%d" % (width, height, posx, posy))

lbTitle = Label(root, text=los.finish(), font=("Arial", 12))
lbTitle.place(x=200, y=10)

enPath = Entry(root, font=("Arial", 12), width=30)
enPath.place(x=80, y=50, height=26)
enPath.insert(0, drive + "/")
enPath.configure(state='disabled')

btnBrowse = layout.HoverButton(root, text=los.browse(), activebackground='#fcf5ff', width=14, height=1, command=browseFiles)
btnBrowse.place(x=400, y=50)

btnCancel = layout.HoverButton(root, text=los.cancel(), activebackground='#fcf5ff', width=12, height=1, command=sys.exit)
btnCancel.place(x=500, y=370)

root.mainloop()
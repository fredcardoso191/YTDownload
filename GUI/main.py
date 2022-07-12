import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from validation import isValidURL
import language_os as los
import getpass
import pathlib

drive = pathlib.Path.home().drive
user = getpass.getuser()

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

def main():
    def video(enUrl):
        url = enUrl.get()
        if isValidURL(url) == False:
            messages(los.invalidurl())
        else:
            try:
                yt = YouTube(url)
                path = f"{drive}/Users/{user}/Videos"
                yt.streams.get_highest_resolution().download(output_path = path)
                messages(los.successfuldownload())
            except:
                messages(los.downloaderror())
    
    def audio(enUrl):
        url = enUrl.get()
        if isValidURL(url) == False:
            messages(los.invalidurl())
        else:
            try:
                yt = YouTube(url)
                path = f"{drive}/Users/{user}/Music"
                yt.streams.filter(only_audio=True).first().download(output_path = path)
                messages(los.successfuldownload())
            except:
                messages(los.downloaderror())
    
    def messages(m):
        if m == los.invalidurl():
            messagebox.showwarning(los.title(), m)
        if m == los.downloaderror():
            messagebox.showerror(los.title(), m)
        if m == los.successfuldownload():
            messagebox.showinfo(los.title(), m)
        root.mainloop()

    def on_click(event):
        enUrl.configure(state=NORMAL)
        enUrl.delete(0, END)
        enUrl.unbind('<Button-1>', on_click_id)

    root = Tk()

    root.resizable(width=False, height=False)
    root.title("Youtube Download")
    root.iconbitmap('icon.ico')

    width = 700
    height = 50

    width_screen = root.winfo_screenwidth()
    height_screen = root.winfo_screenheight()

    posx = width_screen/2 - width/2
    posy = height_screen/3 - height/3

    root.geometry("%dx%d+%d+%d" % (width, height, posx, posy))

    enUrl = Entry(root, width=400, font="Arial")
    enUrl.pack(ipady=1)
    enUrl.insert(0, "https://www.youtube.com/watch?v=")
    enUrl.configure(state=DISABLED)

    on_click_id = enUrl.bind('<Button-1>', on_click)

    btnVideo = HoverButton(root, text=los.button("video"), activebackground='#fcf5ff', command=lambda: video(enUrl)).place(x=0, y=24)
    btnAudio = HoverButton(root, text=los.button("audio"), activebackground='#fcf5ff',command=lambda: audio(enUrl)).place(x=95, y=24)

    root.mainloop()
main()
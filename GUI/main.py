from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from validation import isValidURL
import language_os as los
import getpass

user = getpass.getuser()

def main():
    def video(enUrl):
        url = enUrl.get()
        if isValidURL(url) == False:
            messages(los.invalidurl())
        else:
            try:
                yt = YouTube(url)
                path = f"C:/Users/{user}/Videos"
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
                path = f"C:/Users/{user}/Music"
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
    root.geometry("700x50")

    enUrl = Entry(root, width=400, font="Arial")
    enUrl.pack(ipady=1)
    enUrl.insert(0, "https://www.youtube.com/watch?v=")
    enUrl.configure(state=DISABLED)

    on_click_id = enUrl.bind('<Button-1>', on_click)

    btnVideo = Button(root, text=los.button("video"), command=lambda: video(enUrl)).place(x=0, y=24)
    btnAudio = Button(root, text=los.button("audio"),command=lambda: audio(enUrl)).place(x=95, y=24)

    root.mainloop()
main()
import os, winshell, win32com.client

def create(folder_path):
    desktop = winshell.desktop()
    path = os.path.join(desktop, 'Youtube Download.lnk')
    target = folder_path + "/Youtube Download/main.exe"
    icon = folder_path + "/Youtube Download/icon.ico"
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.IconLocation = icon
    shortcut.WorkingDirectory = folder_path + "Youtube Download"
    shortcut.save()
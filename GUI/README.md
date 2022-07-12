# YTDownload GUI (Graphical user interface)

### Create executable file
```
pyinstaller --onefile --noconsole --icon=icon.ico .\main.py
```

### Once completed, the main.exe executable file will be located inside the dist/ folder.
<br>

## Warning
### It is essential that icon.ico is in the same folder as main.exe, else the application will give an error. You can create a shortcut on your desktop and pass the application path to it, remember that you must pass the full path including putting main.exe at the end of it. Once this is done, the application will be functional and ready to use.
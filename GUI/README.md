# YTDownload GUI (Graphical user interface)

## If you don't have the pytube library installed, type in the terminal
```
pip install pytube
```

## To run the program, type in the terminal inside the folder
```
python main.py
```

## If you want to create an executable file

### Install the pyinstaller package
```
pip install pyinstaller
```

### Create executable file
```
pyinstaller --onefile --noconsole --icon=icon.ico .\main.py
```

### Once completed, the main.exe executable file will be located inside the dist/ folder.
<br>

## Warning
### It is essential that icon.ico is in the same folder as main.exe, else the application will give an error. You can create a shortcut on your desktop and pass the application path to it, remember that you must pass the full path including putting main.exe at the end of it. Once this is done, the application will be functional and ready to use.
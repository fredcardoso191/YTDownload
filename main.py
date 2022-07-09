import os
import download
import language_os as los
import validation as va

while True:
    url = str(input(los.enterurl()))

    if url == "quit":
        exit()
    if (va.isValidURL(url) == True):
        op = str(input(los.option())) or '.'
        if op == '1':
            download.video(url)
        if op == '2':
            download.audio(url)
    else:
        print(los.invalidurl(url))
    
    os.system("pause")
    os.system("cls")
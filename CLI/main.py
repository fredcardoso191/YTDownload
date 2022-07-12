import os
import download
import language_os as los
import validation as va

while True:
    url = str(input(los.enterurl()))

    if url == 'quit':
        exit()
    if (va.isValidURL(url) == True):
        while True:
            op = str(input(los.option())) or '.'
            if op == '1':
                download.video(url)
                break
            if op == '2':
                download.audio(url)
                break
            if op == 'quit':
                exit()
            if op == 'back':
                break
            else:
                print(los.invalidoption())
                os.system("pause")
                os.system("cls")
    else:
        print(los.invalidurl(url))
    
    os.system("pause")
    os.system("cls")
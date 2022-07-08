from pytube import YouTube
import getpass
import os
import re

def video(yt, destination):
    try:
        yt.streams.get_highest_resolution().download(output_path = destination)
    except:
        print("Download error.")
    print(yt.title + " has been successfully downloaded.")

def audio(yt, destination):
    try:
        yt.streams.filter(only_audio=True).first().download(output_path = destination)
    except:
        print("Download error.")
    print(yt.title + " has been successfully downloaded.")

def isValidURL(str):
    regex = ("((http|https)://)(www.)(youtube.)(com)?" +
             "[//]" + 
             "(watch)?" +
             "[?v=]" +
             "([-a-zA-Z0-9_])")

    p = re.compile(regex)
 
    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False

while True:
    print("CTRL + C to exit.")
    url = str(input("Enter the URL of the video you want to download: \n>> "))
    
    if (isValidURL(url) == True):
        yt = YouTube(url)
        option = str(input("1- Download video. \n2- Download audio.\n>> ")) or '.'
        user = getpass.getuser()
        if option == '1':
            destination = "C:/Users/" + user + "/Videos"
            video(yt, destination)
        if option == '2':
            destination = "C:/Users/" + user + "/Music"
            audio(yt, destination)
    else:
        print(f"Invalid URL ({url}). Enter the valid URL (https://www.youtube.com/watch?v=...)")
    
    os.system("pause")
    os.system("cls")
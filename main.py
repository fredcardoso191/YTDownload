from pytube import YouTube
import getpass
import os

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

yt = YouTube(
        str(input("Enter the URL of the video you want to download: \n>> "))
)

option = str(input("1- Download video. \n2- Download audio.\n>> ")) or '.'

user = getpass.getuser()

if option == '1':
    destination = "C:/Users/" + user + "/Videos"
    video(yt, destination)
if option == '2':
    destination = "C:/Users/" + user + "/Music"
    audio(yt, destination)

os.system("pause")
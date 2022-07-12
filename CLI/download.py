from pytube import YouTube
import language_os as los
import getpass

def video(url):
    user = getpass.getuser()
    path = f"C:/Users/{user}/Videos"
    yt = YouTube(url)
    try:
        yt.streams.get_highest_resolution().download(output_path = path)
        print(yt.title + los.successfuldownload())
    except:
        print(los.downloaderror())

def audio(url):
    user = getpass.getuser()
    path = f"C:/Users/{user}/Music"
    yt = YouTube(url)
    try:
        yt.streams.filter(only_audio=True).first().download(output_path = path)
        print(yt.title + los.successfuldownload())
    except:
        print(los.downloaderror())
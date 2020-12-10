import pytube
import os

def DownloadVideo(): 
    Video = input("Input Video URL:") #Do not include &abChannel=*
    try:
        ytVideo = pytube.YouTube(Video)
    except:
        print("Invalid URL")
        DownloadVideo()
    print("Fetching . . .")
    with open("DownloadPath.txt") as fp:
        for i, line in enumerate(fp):
            if i == 1:
                Path = line
    print("Downloading . . .")
    ytStream = ytVideo.streams.first()
    ytStream.download(Path)
    print("Completed!")
    DownloadVideo()
DownloadVideo()
os.system("pause")

from pytube import YouTube
from sys import argv

link=argv[1]
yt=YouTube(link)

print("Titile :",yt.title)

print("Views :",yt.views)

ytd=yt.streams.get_highest_resolution()

ytd.download('D:\selected')

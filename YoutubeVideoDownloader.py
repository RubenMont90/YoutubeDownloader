from pytube import YouTube
from sys import argv

dwnldpath = "C:\\Users\\RM\\Downloads\\YouTube"

link = argv[1]
yt = YouTube(link)

#print("Title: ", yt.title)
#print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download(dwnldpath)

from __future__ import unicode_literals
import youtube_dl

x = input("Video Address:")
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([x])
print("The file is located at the dictory of the script")
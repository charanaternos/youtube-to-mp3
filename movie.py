from logging import exception
from turtle import st

import yt_dlp

# 1. ask the user to paste the youtube url
url = input("Please paste the YouTube URL: ")
# 2. tell the downloder we ONLY want the best audio, converted to MP3
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
# this automatically names the file after the youtube vodeo's actual title!
    'outtmpl': '%(title)s.%(ext)s',
}
# 3. download the video and convert it to mp3
print("\ndownloading and converting... please wait.")

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("\nDone! Check your current directory for the mp3 file.")


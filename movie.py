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
    print("\nDownload and conversion complete!")
except Exception as e:
    print(f"An error occurred: {e}")
# 4. create download button for the user to click and download the mp3 file
# (This part is not applicable in a command-line environment, but in a web application, you would generate a download link for the user to click.)
st.write("\nYour MP3 file is ready! Please check your current directory for the downloaded file.")
st.write("Thank you for using the YouTube to MP3 converter!")
exception as e:
st.error(f"An error occurred: {e}")
else:
st.warning ("Please enter a valid YouTube URL.")


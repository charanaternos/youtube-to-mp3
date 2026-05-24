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
print("\ndownloading and converting... please wait...\n")
# 4. handle any exceptions that may occur during the download process
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("\nDownload and conversion complete!")
except yt_dlp.utils.DownloadError as e:
    print(f"\nAn error occurred during the download process: {e}")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
# 5.create the download button
with open ("audio.mp3" , "rb") as f:
    st.__eq__
# 6. inform the user that the process is complete and where to find the mp3 file
print("\nThe MP3 file has been saved in the current directory.")
# 7. ask the user if they want to download another video
while True:
    again = input("\nDo you want to download another video? (yes/no): ").strip().lower()
    if again == 'yes':
        url = input("Please paste the YouTube URL: ")
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("\nDownload and conversion complete!")
        except yt_dlp.utils.DownloadError as e:
            print(f"\nAn error occurred during the download process: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
        print("\nThe MP3 file has been saved in the current directory.")
    elif again == 'no':
        print("\nThank you for using the YouTube to MP3 converter. Goodbye!")
        break
    else:
        print("\nInvalid input. Please enter 'yes' or 'no'.")
# 8. end the program         
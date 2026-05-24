import streamlit as st
import yt_dlp

st.title("Simple YouTube Downloader")
url = st.text_input("Paste YouTube Link:")

# 1. Let the user choose between Video or Audio
format_choice = st.radio("Select format:", ["Audio (MP3)", "Video (MP4)"])

# 2. Show different quality options depending on the format chosen
if format_choice == "Audio (MP3)":
    quality_choice = st.selectbox("Audio Quality:", ["192 (High)", "128 (Standard)", "64 (Low)"])
else:
    quality_choice = st.selectbox("Video Quality:", ["1080", "720", "480", "360"])

if st.button("Convert & Download"):
    if url:
        with st.spinner("Downloading... please wait!"):
            
            # 3. Set the settings based on the user's choices
            if format_choice == "Audio (MP3)":
                # Get just the number (e.g., "192") from the drop-down selection
                bitrate = quality_choice.split(" ")[0] 
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': bitrate}],
                    'outtmpl': 'output.%(ext)s'
                }
                final_file = "output.mp3"
                
            else: # Video (MP4)
                height = quality_choice # "1080", "720", etc.
                ydl_opts = {
                    # This tells yt-dlp to grab video up to the selected height + the best audio
                    'format': f'bestvideo[height<={height}]+bestaudio/best[height<={height}]',
                    'merge_output_format': 'mp4',
                    'outtmpl': 'output.%(ext)s'
                }
                final_file = "output.mp4"

            # 4. Run the download
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                # 5. Create the download button
                with open(final_file, "rb") as file:
                    st.download_button(label=f"Save {format_choice}", data=file, file_name=final_file)
                    
            except Exception as e:
                st.error(f"Error: {e}")
                
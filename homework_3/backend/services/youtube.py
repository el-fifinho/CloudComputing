import yt_dlp
import os

def download_audio_from_youtube(url):
    output_path = "temp/audio.mp3"
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': "C:\\Users\\plama\\Desktop\\An 3\\Semestrul 2\\Cloud Computing\\Homeworks\\Homew3cuTudorRoman\\ffmpeg-2025-03-31-git-35c091f4b7-full_build\\ffmpeg-2025-03-31-git-35c091f4b7-full_build\\bin\\ffmpeg.exe"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output_path
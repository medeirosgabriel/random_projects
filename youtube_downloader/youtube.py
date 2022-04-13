import os
import youtube_dl

def download(link, name):

    finalName = "{0}.{1}".format(name, "mp3")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': finalName,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            filenames = [link]
            ydl.download(filenames)
    except:
        os.system("clear")
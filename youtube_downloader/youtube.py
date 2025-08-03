import yt_dlp

def downloadMusic(link, name):

    directory = "./music"

    path =  f"{directory}/{name}"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        filenames = [link]
        ydl.download(filenames)

def downloadVideo(link, name):
    download_directory = './video'

    video_info = yt_dlp.YoutubeDL().extract_info(
		url = link, download = False
	)
    
    path = f'{download_directory}/{name}.mp4'

    ydl_opts = {
        'outtmpl': path,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'merge_output_format': 'mp4',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_info['webpage_url']])
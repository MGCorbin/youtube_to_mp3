from __future__ import unicode_literals
import youtube_dl

dl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def download(ipt):
    with youtube_dl.YoutubeDL(dl_opts) as ydl:
        ydl.download([ipt])
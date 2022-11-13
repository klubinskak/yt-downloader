from tkinter import PhotoImage
from pytube import Playlist, YouTube


def download_highest_resoulution(link, user_path):
    print('Downloading..')
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    print("Done! Enjoy!")
    yd.download(user_path)


def download_audio_mp4(link, user_path):
    yt = YouTube(link)
    print("Downloading...")
    yd = yt.streams.get_audio_only()
    subName = yd.default_filename.split('.')
    fileName = subName[0] + '-audio.' + subName[1]
    print(fileName)
    yd.download(user_path, fileName)
    print("Done! Enjoy!")


def download_playlist(link, user_path):
    playlist = Playlist(link)
    results = playlist.video_urls
    print('Loading videos...')
    print(results)

    for item in results:
        download_audio_mp4(item)



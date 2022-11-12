from pytube import YouTube, Playlist

def download_highest_resoulution(link):
    print('Downloading..')
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    print("Done! Enjoy!")
    yd.download(r'C:\Users\Klaudia\PycharmProjects\python\yt-downloader\download-files')


def download_mp3(link):
    yt = YouTube(link)
    print("Downloading...")
    yd = yt.streams.get_audio_only()
    yd.download(r'C:\Users\Klaudia\PycharmProjects\python\yt-downloader\download-files')
    print("Done! Enjoy!")


def downloadPlaylist(link):
    playlist = Playlist(link)
    results = playlist.video_urls
    print('Loading videos...')
    print(results)

    for item in results:
        download_mp3(item)



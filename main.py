from videofunctions import download_highest_resoulution, download_mp3, downloadPlaylist

print("Welcome in Youtube Downloader by Klubini!")
print("What do you want to do with video?")
print("1.Download video")
print("2.Download mp3")
print("3.Download Playlist")
option = input("Provide number:")
print("Provide link:")
link = input()

if option == '1':
    download_highest_resoulution(link)
elif option == '2':
    download_mp3(link)
else:
    downloadPlaylist(link)



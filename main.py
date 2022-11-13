from tkinter import *
from tkinter import filedialog
from videofunctions import download_highest_resoulution, download_audio_mp4, download_playlist
import pathlib


#Creating window
screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()
current_directory = str(pathlib.Path().absolute()) + '/downloads'


#Functions
def select_path():
    #allows user to select path from the explorer 
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_video():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    if(user_path == ""):
        user_path = current_directory
    first = first_checked.get()
    second = scd_checked.get()
    print(second)
    third = thrd_checked.get()
    if(first == 1):
        download_audio_mp4(get_link, user_path)
    elif (second == 1):
        download_highest_resoulution(get_link, user_path)
    elif( third == 1):
        download_playlist(get_link, user_path)


#image logo
logo_img = PhotoImage(file='./assets/yt-logo.png')
#resize logo to fit in window
logo_img = logo_img.subsample(12, 10)

canvas.create_image(250, 80, image=logo_img)

canvas.create_text(250, 160, text="Welcome in Youtube Downloader", font=('Georgia', 15))
canvas.create_text(250, 180, text="By Klubini! 🚀", font=('Georgia', 15))

#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text='Enter link here:', font=('Georgia', 14))
#adding field to widget
canvas.create_window(250, 210, window=link_label)
canvas.create_window(250, 240, window=link_field)


path_label = Label(screen, text= current_directory, font=('Georgia', 14))
select_btn = Button(screen, text="Select", command=select_path, font=('Georgia', 14))

canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 310, window=select_btn)

first_checked = IntVar()
scd_checked = IntVar()
thrd_checked = IntVar()
first_checkbox = Checkbutton(screen, text="1.Download mp3", variable=first_checked, font=('Georgia', 14))
scd_checkbox = Checkbutton(screen, text="2.Download mp4", variable=scd_checked, font=('Georgia', 14))
thrd_checkbox = Checkbutton(screen, text="3.Download playlist", variable=thrd_checked, font=('Georgia', 14))

canvas.create_window(250, 345, window=first_checkbox)
canvas.create_window(250, 370, window=scd_checkbox)
canvas.create_window(250, 395, window=thrd_checkbox)


download_btn = Button(screen, text="Download File", command=download_video, font=('Georgia', 14))

canvas.create_window(250, 440, window=download_btn)


canvas.create_text(250, 480, text="Made with ♥️ in Poland")


screen.mainloop()
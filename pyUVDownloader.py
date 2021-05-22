
"""
Author : Manendra Nath Shukla
Developed for Educational Purpose 
Project Name : Youtube Video Downloader - pyUVdownloader
Version : 1.0.0
Youtube Channel : MyCodeWorks

"""


from tkinter import filedialog
from tkinter import *
from pytube import YouTube

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

def popupmsg(msg):
    popup = Tk()
    popup.wm_title("Download Status")
    label = Label(popup, text=msg, font=8)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()




def downloadVideo():
    yt=YouTube(e1.get())
    ss=yt.streams.get_highest_resolution().download(folder_path.get())
    popupmsg("Downloded Successfully, visit to this directory : "+str(ss))
    
root = Tk()
root.title('Youtube Video Downloader - Developed By : Manendra Nath Shukla')
img = PhotoImage(file='C:/Users/Manendra Nath Shukla/Desktop/tutorialProject/newlogo.png')
root.wm_iconphoto(True, img)
folder_path = StringVar()
userRes=StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=1, column=1)

Label(root,text="Enter Video Url : ").grid(row=0)
e1 = Entry(root)
e1.grid(row=0, column=1)
Label(root,text="Save to :").grid(row=1)
button2 = Button(text="Browse", command=browse_button , bg='blue')
button2.grid(row=1, column=3)
Label(root,text="Please have some patience dowloading takes time, Once completed you will be notified!!!").grid(row=2)

button3 = Button(root,text="Download", command=downloadVideo,bg='green')
button3.grid(row=4, column=3)



mainloop()




# Another Library  if pytube is not working
# Code to Download the video in mp4

# from __future__ import unicode_literals
# import youtube_dl

# ydl_opts = {
#     'format':' bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4',
#     'outtmpl': 'FULL_LOCATION_TO_OUTPUT_FOLDER/%(title)s.%(ext)s'),
# }

# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             ydl.download(["https://www.youtube.com/watch?v=gSHlCaG78rc"])













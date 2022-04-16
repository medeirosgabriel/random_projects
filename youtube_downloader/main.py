from tkinter import *
from youtube import downloadMusic, downloadVideo
from threading import Thread

root = Tk()
root.title('YouTube Downloader')
root.resizable(100, 100)

# ========== LABELS ==========

Label (
    root, 
    text="YouTube Video URL: ", 
    font=('Aerial 15 bold')
).grid(column=0, row=1, sticky=W, padx=2, pady=2)

e1 = Entry(root, width=50)
e1.grid(column=1, row=1, sticky=W, padx=2, pady=2)

Label (
    root, 
    text="Music/Video Name: ", 
    font=('Aerial 15 bold')
).grid(column=0, row=2, sticky=W, padx=2, pady=2)

e2 = Entry(root, width=50)
e2.grid(column=1, row=2, sticky=W, padx=2, pady=2)

row_index = 5
threads = []

# ========== DOWNLOAD ==========

class DownloadThread(Thread):
    def __init__(self,url,name,download):
        Thread.__init__(self)
        self.url = url
        self.name = name
        self.download = download

    def run(self):
        self.download(self.url, self.name)


def myClickMusic():

    global row_index, threads
    global e1, e2

    url = e1.get()
    name = e2.get()

    msg = "Audio - Youtube ID: " + url.split("=")[1]
    Label (
        root, 
        text=msg,
        font=('Aerial 10 bold')
    ).grid(column=0, row=row_index, sticky=W, padx=2, pady=2)

    msg = "Name: " + name
    Label (
        root, 
        text=msg,
        font=('Aerial 10 bold')
    ).grid(column=1, row=row_index, sticky=W, padx=2, pady=2)

    row_index += 1
    
    thread = DownloadThread(url, name, downloadMusic)
    threads.append(thread)
    thread.start()

    e1.delete(0, 'end')
    e2.delete(0, 'end')

def myClickVideo():

    global row_index, threads
    global e1, e2

    url = e1.get()
    name = e2.get()

    msg = "Video - Youtube ID: " + url.split("=")[1]
    Label (
        root, 
        text=msg,
        font=('Aerial 10 bold')
    ).grid(column=0, row=row_index, sticky=W, padx=2, pady=2)

    msg = "Name: " + name
    Label (
        root, 
        text=msg,
        font=('Aerial 10 bold')
    ).grid(column=1, row=row_index, sticky=W, padx=2, pady=2)

    row_index += 1

    '''
    thread = DownloadThread(url, name, downloadVideo)
    threads.append(thread)
    thread.start()
    '''

    downloadVideo(url, name)

    e1.delete(0, 'end')
    e2.delete(0, 'end')

# ========== BUTTONS ==========

Button (
    root, 
    text='Quit', 
    command=root.quit
).grid(row=3, column=0, sticky=NW, padx=2, pady=2)

Button (
    root, 
    text='Download Audio', 
    command=myClickMusic
).grid(row=3, column=1, sticky=NW,  padx=2, pady=2)

Button (
    root, 
    text='Download Video', 
    command=myClickVideo
).grid(row=4, column=1, sticky=NW,  padx=2, pady=2)

# ========== RUNNING ==========

root.mainloop()

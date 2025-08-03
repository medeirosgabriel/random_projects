from tkinter import *
from youtube import downloadMusic, downloadVideo
from threading import Thread
from PIL import Image, ImageTk


root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.rowconfigure(2, weight=1)
root.columnconfigure(2, weight=1)

root.title('YouTube Downloader')

image = Frame(root)
image.grid(row=0, column=1)

contents = Frame(root)
contents.grid(row=1, column=1)

# ========== LABELS ==========

img = Image.open("./assets/youtube_downloader_logo.png")
img = img.resize((400, 150))
img = ImageTk.PhotoImage(img)

Label(
    image, 
    image = img
).grid(column=0, row=0, sticky="nsew", padx=10, pady=2)

Label (
    contents, 
    text="YouTube Video URL: ", 
    font=('Aerial 15 bold')
).grid(column=0, row=1, sticky=W, padx=10, pady=2)

e1 = Entry(contents, width=50)
e1.grid(column=1, row=1, sticky=W, padx=10, pady=2)

Label (
    contents, 
    text="Music/Video Name: ", 
    font=('Aerial 15 bold')
).grid(column=0, row=2, sticky=W, padx=10, pady=2)

e2 = Entry(contents, width=50)
e2.grid(column=1, row=2, sticky=W, padx=10, pady=2)

# =========== LISTBOX ==========

my_listbox = Listbox(contents)
my_listbox.grid(row=5, columnspan=2, sticky='nsew', padx=10, pady=2)

# ========== DOWNLOAD ==========

threads = []

class DownloadThread(Thread):
    def __init__(self,url,name,download):
        Thread.__init__(self)
        self.url = url
        self.name = name
        self.download = download

    def run(self):
        self.download(self.url, self.name)

def myClickMusic():

    global threads
    global e1, e2

    url = e1.get()
    name = e2.get()

    msg = "Audio - Youtube ID: " + url.split("=")[1] + " Name: " + name
    my_listbox.insert(END, msg)
    
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

    msg = "Video - Youtube ID: " + url.split("=")[1] + " Name: " + name
    my_listbox.insert(END, msg)

    thread = DownloadThread(url, name, downloadVideo)
    threads.append(thread)
    thread.start()

    e1.delete(0, 'end')
    e2.delete(0, 'end')

# ========== BUTTONS ==========

Button (
    contents, 
    text='Quit', 
    command=root.quit
).grid(row=3, column=0, sticky=NW, padx=10, pady=2)

Button (
    contents, 
    text='Download Audio', 
    command=myClickMusic
).grid(row=3, column=1, sticky=NW,  padx=10, pady=2)

Button (
    contents, 
    text='Download Video', 
    command=myClickVideo
).grid(row=4, column=1, sticky=NW,  padx=10, pady=2)

# ========== RUNNING ==========

root.mainloop()

from tkinter import *
import socket
from threading import Thread

# ============== INTERFACE ==============

root = Tk()
root.title('Chat Book')
root.resizable(100, 100)

frame = Frame(root)
frame.columnconfigure(0, weight=2)
frame.columnconfigure(1, weight=1)
frame.pack(padx=2, pady=2)

text = Entry(root, width=50)
text.pack(padx=2, pady=2, fill=BOTH)

# ========= CONNECTION CONFIGURATION =========

LOCALHOST = "127.0.0.1"
PORT = 8090
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((LOCALHOST, PORT))
except:
    client.connect((LOCALHOST, PORT + 1))

row = 0

class DataReceiver (Thread):

    def __init__(self, clientSocket, frame):
        self.socket = clientSocket
        self.frame = frame
        self.stop_thread = False
        Thread.__init__(self)

    def run(self):
        global row
        while not self.stop_thread:
            data = self.socket.recv(1024)
            if not data: 
                break
            msg = data.decode()
            label = Label(self.frame, text=msg, justify='left')
            label.config(bg="#abff68", font=('Helvatical bold',12))
            label.grid(row=row, column=0, pady=2)
            #label.pack()
            row += 1

    def stop(self):
        self.stop_thread = True

dataReceiver = DataReceiver(client, frame)
dataReceiver.start()

def send_message():
    global text, client, frame, row
    msg = text.get()
    label = Label(frame, text=msg, justify='right')
    label.config(bg="#00faff", font=('Helvatical bold',12))
    label.grid(row=row, column=1, pady=2)
    #label.pack()
    row += 1
    client.sendall(text.get().encode())
    text.delete(0, 'end')

# ============== BUTTONS ==============

Button (
    root, 
    text='Send', 
    command=send_message,
).pack(padx=2, pady=2, fill=BOTH)

def quit():
    global dataReceiver, root
    print("ok")
    dataReceiver.stop()
    root.quit()

Button (
    root, 
    text='Quit',
    command=quit
).pack(padx=2, pady=2, fill=BOTH)

root.mainloop()
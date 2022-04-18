from tkinter import *
from email_util import send_email

root = Tk()
root.title('Send Email')
root.resizable(100, 100)

# ========== LABELS ==========

Label (
    root, 
    text="Gmail User: ", 
    font=('Aerial 15 bold')
).grid(column=0, row=1, sticky=W, padx=2, pady=2)

e1 = Entry(root, width=50)
e1.grid(column=1, row=1, sticky=W, padx=2, pady=2)

Label (
    root, 
    text="Password: ", 
    font=('Aerial 15 bold')
).grid(column=0, row=2, sticky=W, padx=2, pady=2)

e2 = Entry(root, width=50)
e2.grid(column=1, row=2, sticky=W, padx=2, pady=2)

Label (
    root, 
    text="To: ", 
    font=('Aerial 15 bold')
).grid(column=0, row=3, sticky=W, padx=2, pady=2)

e3 = Entry(root, width=50)
e3.grid(column=1, row=3, sticky=W, padx=2, pady=2)

Label (
    root, 
    text="Subject: ", 
    font=('Aerial 15 bold')
).grid(column=0, row=4, sticky=W, padx=2, pady=2)

e4 = Entry(root, width=50)
e4.grid(column=1, row=4, sticky=W, padx=2, pady=2)


Label (
    root, 
    text="Text: ", 
    font=('Aerial 15 bold')
).grid(column=0, row=5, sticky=W, padx=2, pady=2)

e5 = Entry(root, width=50)
e5.grid(column=1, row=5, sticky=W, padx=2, pady=2)


# ========== Send Function ==========

def send_func():
    gmail_user = e1.get()
    gmail_password = e2.get()
    recipient = e3.get()
    subject = e4.get()
    body = e5.get()
    send_email(gmail_user, recipient, gmail_password, subject, body)
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')

# ========== BUTTONS ==========

Button (
    root, 
    text='Quit', 
    command=root.quit
).grid(row=6, column=0, sticky=NW, padx=2, pady=2)

Button (
    root, 
    text='Send Email', 
    command=send_func
).grid(row=6, column=1, sticky=NW,  padx=2, pady=2)

# ========== RUNNING ==========

root.mainloop()

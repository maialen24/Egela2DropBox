import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import PIL

import funtzioak
import Dropbox as dBox



def downloadw():
    window = Tk()
    window.title("Download")
    window.geometry('550x400')

    lbl = Label(window, text="Path", font=(14))
    lbl.place(x=50, y=100)

    path = Entry(window, width=30)
    path.place(x=90, y=100)


def error():
    window = Tk()
    window.title("Error")
    window.geometry('300x200')
    lbl = Label(window, text="Invalid url",font=("Arial Bold", 16))
    lbl.pack()

def DropBox():
    window = Tk()
    window.title("DropBox")
    window.geometry('800x400')
    files = Listbox(window, width=700, height=400, selectmode=EXTENDED)
    files.pack()


    dBox.Dropbox.list_files(files)

def html2pdfW():
    window = Tk()
    window.title("HTML TO PDF")
    window.geometry('550x400')
    lbl = Label(window, text="URL",font=(14))

    lbl.place(x=50,y=100)
    url= Entry(window, width=30)
    url.place(x=90,y=100)


    path = Entry(window, width=20,state='disabled')
    path.place(x=120, y=200)

    lpath = Label(window, text="Path:", font=(14))
    lpath.place(x=50, y=200)

    def callbackFunc(event):
        if combo.get()=='Local':
            path["state"] = "normal"
        else:
            path["state"] = "disabled"
            #combo.config(state='normal')


    combo=Combobox(window,values=['Local', 'DropBox'],width=10)
    combo['state'] = 'readonly'
    combo.place(x=340,y=100)

    combo.bind("<<ComboboxSelected>>", callbackFunc)

    def clicked():
        if combo.get()=='DropBox':
            gorde=''
        else:
            gorde=path.get()


        funtzioak.html2pdf(url.get(),gorde,combo.get())
       # img = PhotoImage(PIL.Image.open('check.png'))
       # irudia= Label(window,image=img)
       # irudia.place(x=300,y=200)
       # time.sleep(6)
       # irudia.place_forget()
       # messagebox.showinfo('Message title', 'Message content')


    btn = Button(window, text="Download", command=clicked)
    btn.place(x=450,y=100)
   # btn.grid(column=2, row=0)



def allFiles():
    window = Tk()
    window.title("Get files")
    window.geometry('800x700')
    lbl = Label(window, text="URL")
    lbl.place(x=20,y=100)
    url = Entry(window, width=50)
    url.place(x=50, y=100)

    lb = Listbox(window, width=50, height=30, selectmode=EXTENDED)
    lb.place(x=50, y=150)

    def clicked():
        lista=funtzioak.get_url_paths(url,'pdf')
        print(lista)
        #lista = funtzioak.getAllLinks(url.get())
        if len(lista)==0:
            lb.insert(0,'No files to download')
        else:
            for file in range(0,len(lista)):
                lb.insert(lista[file],file)

    # messagebox.showinfo('Message title', 'Message content')

    btn = Button(window, text="Search", command=clicked)
    btn.place(x=500, y=100)
    def outlook():
        print('outlook')
    def download():
        downloadw()
    def dropbox():
        print('dropbox')

    btnDownload = Button(window, text="Download", command=download)
    btnDownload.place(x=500, y=250)
    btnDropbox = Button(window, text="Dropbox", command=dropbox)
    btnDropbox.place(x=500, y=300)


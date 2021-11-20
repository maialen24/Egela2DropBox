from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import funtzioak


def html2pdfW():
    window = Tk()
    window.title("HTML TO PDF")
    window.geometry('550x400')
    lbl = Label(window, text="URL")
    lbl.grid(column=0, row=0)
    url= Entry(window, width=10)
    url.grid(column=1, row=0)

    def clicked():
        funtzioak.html2pdf(url.get())
       # messagebox.showinfo('Message title', 'Message content')


    btn = Button(window, text="Download", command=clicked)
    btn.grid(column=2, row=0)



def allFiles():
    window = Tk()
    window.title("Get files")
    window.geometry('800x700')
    lbl = Label(window, text="URL")
    lbl.grid(column=0, row=0)
    url = Entry(window, width=10)
    url.grid(column=1, row=0)

    lb = Listbox(window, width=50, height=20, selectmode=EXTENDED)
    lb.grid(column=8, row=6)

    def clicked():
        lista = funtzioak.getAllLinks(url.get())
        for file in range(0,len(lista)):
            lb.insert(lista[file],file)

    # messagebox.showinfo('Message title', 'Message content')

    btn = Button(window, text="Search", command=clicked)
    btn.grid(column=2, row=0)
    def outlook():
        print('outlook')
    def download():
        print('download')
    def dropbox():
        print('dropbox')
    btnOutlook = Button(window, text="Outlook", command=outlook)
    btnOutlook.grid(column=8, row=4)
    btnDownload = Button(window, text="Download", command=download)
    btnDownload.grid(column=8, row=6)
    btnDropbox = Button(window, text="Dropbox", command=dropbox)
    btnDropbox.grid(column=8, row=8)


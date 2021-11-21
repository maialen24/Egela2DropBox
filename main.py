from tkinter import *
from PIL import ImageTk, Image
from cffi.setuptools_ext import execfile

import OptionWindows
import zeregina4

window = Tk()

window.title("Welcome to Egela2DropBox")

window.geometry('450x400')
path='./logoEgela2Dropbox.png'
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
label = Label(window)
label.grid(column=20, row=0)

titulo= Label(window, text='Egela2DropBox',font=("Arial Bold", 50))
titulo.grid(column=200,row=0)
#lbl = Label(window, text="Egela2DropBox")

#lbl.grid(column=0, row=0)

txt = ''

#txt.grid(column=1, row=0)

def clickedEgela():
    zeregina4.egela2drop()
    #exec(open("./zeregina4.py").read())

   # execfile("zeregina4.py")
    #print()



btnEgela = Button(window, text="Egela", height = 5, width = 10,command=clickedEgela)
btnEgela.grid(column=200, row=8)



def clickedGetfitx():

    OptionWindows.allFiles()


btnGetfitx= Button(window, text="Get files",height = 5, width = 10, command=clickedGetfitx)

btnGetfitx.grid(column=200, row=12)

def clickedWeb2html():

    OptionWindows.html2pdfW()



btnWeb2html= Button(window, text="Web to pdf",height = 5, width = 10, command=clickedWeb2html)

btnWeb2html.grid(column=200, row=14)



window.mainloop()

#main ventana, con botones opciones

import get
#import eGela
#egela=eGela()
#egela.pdf('https://www.ehu.eus/eu/web/nazioarteko-harremanak/2021-2022-mugikortasun-plazak-berresleitzeko-baimenaren-ebazpena')

# Import libraries
import requests
from bs4 import BeautifulSoup

# URL from which pdfs to be downloaded
#url = "https://www.geeksforgeeks.org/how-to-extract-pdf-tables-in-python/"
#url='https://www.ehu.eus/eu/web/nazioarteko-harremanak/2021-2022-mugikortasun-plazak-berresleitzeko-baimenaren-ebazpena'

import os
import urllib

# connect to website and get list of all pdfs
#url="http://www.gatsby.ucl.ac.uk/teaching/courses/ml1-2016.html"
#response = request.urlopen(url).read()
#soup= BeautifulSoup(response, "html.parser")
#links = soup.find_all('a', href=re.compile(r'(.pdf)'))


# clean the pdf link names
#url_list = []
#for el in links:
#    if(el['href'].startswith('http')):
   #     url_list.append(el['href'])
    #else:
     #   url_list.append("http://www.gatsby.ucl.ac.uk/teaching/courses/" + el['href'])

#print(url_list)


# download the pdfs to a specified location
#for url in url_list:
  #  print(url)
  #  fullfilename = os.path.join('.',url) #url.replace("http://www.gatsby.ucl.ac.uk/teaching/courses/ml1-2016/", ""))
  #  print(fullfilename)
  #  request.urlretrieve(url, fullfilename)
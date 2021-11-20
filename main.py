from cffi.setuptools_ext import execfile
from kivy.app import App
from functools import partial
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from kivy.properties import NumericProperty, ReferenceListProperty, \
 \
    ObjectProperty

from kivy.vector import Vector

from kivy.clock import Clock
from kivy.uix.label import Label
from urllib import request
from bs4 import BeautifulSoup
import re
from tkinter import *
from PIL import ImageTk, Image
import OptionWindows



window = Tk()

window.title("Welcome to Egela2DropBox")

window.geometry('350x200')
path='./logoEgela2Dropbox.png'
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
label = Label(window, image = img)
label.grid(column=20, row=0)

#lbl = Label(window, text="Egela2DropBox")

#lbl.grid(column=0, row=0)

txt = ''

#txt.grid(column=1, row=0)

def clickedEgela():
    #execfile("zeregina4.py")
    print()



btnEgela = Button(window, text="Egela", command=clickedEgela)
btnEgela.grid(column=5, row=2)

def clickedDropbox():

    res = "Welcome to " + txt.get()



btnDropBox= Button(window, text="DropBox", command=clickedDropbox)

btnDropBox.grid(column=5, row=4)

def clickedGetfitx():

    res = "Welcome to " + txt.get()


btnGetfitx= Button(window, text="Get files", command=clickedGetfitx)

btnGetfitx.grid(column=5, row=6)

def clickedWeb2html():

    OptionWindows.html2pdfW()



btnWeb2html= Button(window, text="Web to pdf", command=clickedWeb2html)

btnWeb2html.grid(column=5, row=8)



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
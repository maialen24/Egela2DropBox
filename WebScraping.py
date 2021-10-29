
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin


def lortuhtml(uria,cookie):
    metodoa = 'GET'
    goiburuak = {'Cookie': cookie}
    erantzuna = requests.request(metodoa, uria, headers=goiburuak, allow_redirects=False)
    kodea = erantzuna.status_code
    deskribapena = erantzuna.reason
    print(str(kodea) + " " + deskribapena)
    edukia = erantzuna.content

    return edukia


def eskaerak():
    metodoa = 'GET'
    uria = "https://egela.ehu.eus"
    goiburuak = {'Host': 'egela.ehu.eus',
                 'Content-Type': 'application/x-www-form-urlencoded'}
    erantzuna = requests.request(metodoa, uria,
                                 headers=goiburuak, allow_redirects=False)
    kodea = erantzuna.status_code
    deskribapena = erantzuna.reason

    #ESKAERA ETA ERANTZUNAK INPRIMATU
    print("ESKAERA:")
    print(metodoa +' '+ uria)
    print("ERANTZUNA:")
    print(str(kodea) + " " + deskribapena)
    print(erantzuna.headers)

    goiErantzuna=erantzuna.headers
    nora=goiErantzuna['Location']

    #LEHENENGO BIKOTEA BIGARRENA
    metodoa = 'GET'
    uria = nora
    goiburuak = {}
    erantzuna = requests.request(metodoa, uria,
                                 headers=goiburuak, allow_redirects=False)
    kodea = erantzuna.status_code
    deskribapena = erantzuna.reason

    # ESKAERA ETA ERANTZUNAK INPRIMATU
    print("ESKAERA")
    print(metodoa+' '+uria)
    print("ERANTZUNA")
    print(str(kodea) + " " + deskribapena)
    print(erantzuna.headers)


  #BIGARREN BIKOTEA
    # Egelan logeatzeko behar diren datuak lortu
    print("Sartu erabiltzailea:" )
    erabiltzailea = input()
    print("Sartu pasahitza: ")
    pasahitza= input()

    #Eskaera egin
    metodoa ='POST'
    uria=nora
    goiburuak={'Content-Type': 'application/x-www-form-urlencoded'}
    edukia={'username' : erabiltzailea, 'password' : pasahitza}
    edukia_encoded = urllib.parse.urlencode(edukia)
    goiburuak['Content-Length'] = str(len(edukia_encoded))
    erantzuna = requests.request(metodoa, uria, data=edukia_encoded,
                                 headers=goiburuak, allow_redirects=False)
    kodea = erantzuna.status_code
    deskribapena = erantzuna.reason

    # ESKAERA ETA ERANTZUNAK INPRIMATU
    print("ESKAERA")
    print(metodoa +' '+ uria)
    print("ERANTZUNA")
    print(str(kodea) + " " + deskribapena)
    edukia = erantzuna.content
    print(erantzuna.headers)
    cookie=erantzuna.headers['Set-Cookie']
    nora=erantzuna.headers['Location']
    #print(edukia)


    metodoa = 'GET'
    uria= nora
    goiburuak={'Cookie':cookie}
    erantzuna = requests.request(metodoa, uria,
                                 headers=goiburuak, allow_redirects=False)
    kodea = erantzuna.status_code
    deskribapena = erantzuna.reason
    print("ESKAERA")
    print(metodoa+ ' '+uria)
    print("ERANTZUNA")
    print(str(kodea) + " " + deskribapena)
    edukia = erantzuna.content
    print(erantzuna.headers)
    nora=erantzuna.headers['Location']

    metodoa = 'GET'
    uria = nora
    goiburuak = {'Cookie': cookie}
    erantzuna = requests.request(metodoa, uria,
                                 headers=goiburuak, allow_redirects=False)
    kodea = erantzuna.status_code
    deskribapena = erantzuna.reason

    #ESKAERA ETA ERANTZUNA INPRIMATU
    print("ESKAERA")
    print(metodoa+ ' '+ uria)
    print("ERANTZUNA")
    print(str(kodea) + " " + deskribapena)
    edukia = erantzuna.content
    print(erantzuna.headers)
    print(edukia)

    #WEB SISTEMAK IRAKASGAIAN SARTU ETA HTML LORTU
    metodoa = 'GET'
    uria='https://egela.ehu.eus/course/view.php?id=42336'
    goiburuak={'Cookie':cookie}
    erantzuna = requests.request(metodoa, uria,headers=goiburuak, allow_redirects=False)
    kodea = erantzuna.status_code
    deskribapena = erantzuna.reason
    print(str(kodea) + " " + deskribapena)
    edukia = erantzuna.content

    print(erantzuna.headers)
    #print(edukia)

#pdf-ak lortzeko resource daukaten urietan sartu eta barruan .pdf bukatzen dutenak dira
#If there is no such folder, the script will create one automatically
    folder_location = r'C:\Users\usuario\Desktop\WEBsistemak\webscraping'
    if not os.path.exists(folder_location):os.mkdir(folder_location)

    print("PDF-ak aurkitu eta deskargatu")

    soup= BeautifulSoup(edukia, "html.parser")
    print(len(soup.find_all('a','href',class_="")))
    #lortu esteka guztiak
    for link in soup.find_all('a','href',class_=""):
     link=(link['href'])
     #lortu pdf-ak dituztenak
     if(link.startswith('https://egela.ehu.eus/mod/resource')):
      e = lortuhtml(link, cookie)
      s = BeautifulSoup(e, "html.parser")
      for l in s.select("a[href$='.pdf']"):
       current_link=l.get('href')
       izena = current_link.replace(':', '_')
       izena = izena.replace('/', '_')
       print(folder_location+'\\'+izena)
       filename = os.path.join(folder_location, izena)
        # pdf idatzi
       with open(filename, 'wb') as file:
        file.write(lortuhtml(current_link,cookie))


if __name__ == "__main__":
    eskaerak()
import requests
import urllib
from bs4 import BeautifulSoup

print("##### 1. ESKAERA #####")
metodoa = 'POST'
uria = "https://egela.ehu.eus/login/index.php"

headers = {'Host': 'egela.ehu.eus',
           'Content-Type': 'application/x-www-form-urlencoded',}

data = {'username': '',
        'password': ''}

data_encoded = urllib.urlencode(data)
headers['Content-Length'] = str(len(data_encoded))
erantzuna = requests.request(metodoa, uria, headers=headers, data=data_encoded, allow_redirects=False)
print(metodoa + " " + uria)

kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)

cookiea = ""
location = ""

for goiburua in erantzuna.headers:
    print(goiburua + ": " + erantzuna.headers[goiburua])
    if goiburua == "Set-Cookie":
        cookiea = erantzuna.headers[goiburua].split(";")[0]
        print(cookiea)
    elif goiburua == "Location":
        location = erantzuna.headers[goiburua]

edukia = erantzuna.content

print("\n##### 2. ESKAERA #####")
metodoa = 'GET'
uria = location

goiburuak = {'Host': uria.split('/')[2],
             'Cookie': cookiea}

erantzuna = requests.request(metodoa, uria, headers=goiburuak, allow_redirects=False)
print(metodoa + " " + uria)

kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)

for goiburua in erantzuna.headers:
    print(goiburua + ": " + erantzuna.headers[goiburua])
    if goiburua == "Set-Cookie":
        cookiea = erantzuna.headers[goiburua].split(";")[0]
        print(cookiea)
    elif goiburua == "Location":
        location = erantzuna.headers[goiburua]

edukia = erantzuna.content

print("\n##### 3. ESKAERA #####")
metodoa = 'GET'
uria = location

goiburuak = {'Host': uria.split('/')[2],
             'Cookie': cookiea}

erantzuna = requests.request(metodoa, uria, headers=goiburuak, allow_redirects=False)
print(metodoa + " " + uria)

kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)

for goiburua in erantzuna.headers:
    print(goiburua + ": " + erantzuna.headers[goiburua])

edukia = erantzuna.content
print (edukia)

print("\n##### 4. ESKAERA (Ikasgairen eGelako orrialde nagusia) #####")
metodoa = 'GET'
uria = "https://egela.ehu.eus/course/view.php?id=29145"

goiburuak = {'Host': 'egela.ehu.eus',
             'Cookie': cookiea}

erantzuna = requests.request(metodoa, uria, headers=goiburuak, allow_redirects=False)
print(metodoa + " " + uria)

kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)

for goiburua in erantzuna.headers:
    print(goiburua + ": " + erantzuna.headers[goiburua])

edukia = erantzuna.content

print("\n##### HTML-aren azterketa... #####")
soup = BeautifulSoup(edukia, 'html.parser')
item_results = soup.find_all('img', {'class': 'iconlarge activityicon'})

for each in item_results:
    if each['src'].find("/pdf") != -1:
        print("\n##### PDF-a bat aurkitu da! #####")
        pdf_link = each.parent['href']

        uria = pdf_link

        headers = {'Host': 'egela.ehu.eus',
                   'Cookie': cookiea}

        erantzuna = requests.get(uria, headers=headers, allow_redirects=False)
        print(metodoa + " " + uria)

        kodea = erantzuna.status_code
        deskribapena = erantzuna.reason

        print(str(kodea) + " " + deskribapena)
        edukia = erantzuna.content

        soup2 = BeautifulSoup(edukia, 'html.parser')
        div_pdf = soup2.find('div', {'class': 'resourceworkaround'})
        pdf_link = div_pdf.a['href']

        print("\t##### PDF-a deskargatzen... #####")
        uria = pdf_link

        headers = {'Host': 'egela.ehu.eus',
                   'Cookie': cookiea}

        erantzuna = requests.get(uria, headers=headers, allow_redirects=False)
        print("\t" + metodoa + " " + uria)

        kodea = erantzuna.status_code
        deskribapena = erantzuna.reason

        print("\t" + str(kodea) + " " + deskribapena)
        pdf = erantzuna.content

        pdf_izena = pdf_link.split('/')[-1]
        file = open("./pdf/" + pdf_izena, "wb")
        file.write(pdf)
        file.close()






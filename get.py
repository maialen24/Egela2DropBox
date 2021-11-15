#get pdf-s de webs

from tkinter import messagebox
from bs4 import BeautifulSoup
import requests
import urllib
import urllib.parse
import time
import helper

class eGela:
    _login = 0
    _cookiea = ""
    _refs = []
    _root = None

    def get_pdf_refs(self,uria):
        popup, progress_var, progress_bar = helper.progress("get_pdf_refs", "Downloading PDF list...")
        progress = 0
        progress_var.set(progress)
        progress_bar.update()

        print("\n##### 1. ESKAERA (Orrialde nagusia) #####")
        metodoa = 'POST'
        data = ""
        section = 1
        pdf = []
        status = 0
        print("Metodoa: ")
        print(metodoa)
        while status != 404:
           #goiburuak = {'Host': 'egela.ehu.eus', 'Content-Type': 'application/x-www-form-urlencoded', 'Content-Length': str(len(data)), 'Cookie': self._cookiea}
           # uria = "https://egela.ehu.eus/course/view.php?id=42336&section=" + str(section)
            erantzuna = requests.request(metodoa, uria, data=data, allow_redirects=False)
            edukia = erantzuna.content
            status = erantzuna.status_code
            print(status)
            if erantzuna.status_code == 200:
               # print("Web Sistemak")
                soup = BeautifulSoup(erantzuna.content, "html.parser")
                pdf_results = soup.find_all("div", {"class": "activityinstance"})
                kop = str(pdf_results).count("pdf")
                print("PDF kop: " + str(kop))

            print("\n##### HTML-aren azterketa... #####")
            soup = BeautifulSoup(edukia, 'html.parser')
            item_results = soup.find_all('img', {'class': 'iconlarge activityicon'})
            for each in item_results:

                if each['src'].find("/pdf") != -1:
                    print("\n##### PDF-a bat aurkitu da! #####")
                    pdf_link = each.parent['href']
                    uria = pdf_link
                    if pdf.__contains__(uria):
                        print("PDF hau " + uria + " aurkituta dago jada!")
                    else:
                        #headers = {'Host': 'egela.ehu.eus', 'Cookie': self._cookiea}
                        erantzuna = requests.get(uria, allow_redirects=False)
                        status = erantzuna.status_code
                        print(status)
                        if status == 303:
                            pdf_uria = erantzuna.headers['Location']
                            erantzuna = requests.get(pdf_uria, allow_redirects=False)
                            print(metodoa + " " + uria)
                            kodea = erantzuna.status_code
                            deskribapena = erantzuna.reason
                            print(str(kodea) + " " + deskribapena)
                            pdf_link = pdf_uria.split("mod_resource/content/")[1].split("/")[1].replace("%20", "_")
                            pdf_izena = pdf_link.split('/')[-1]
                            self._refs.append({'link': pdf_uria, 'pdf_name': pdf_izena})
                        else:
                            print(metodoa + " " + uria)
                            kodea = erantzuna.status_code
                            deskribapena = erantzuna.reason
                            print(str(kodea) + " " + deskribapena)
                            edukia = erantzuna.content
                            status = erantzuna.status_code
                            soup2 = BeautifulSoup(edukia, 'html.parser')
                            div_pdf = soup2.find('div', {'class': 'resourceworkaround'})
                            pdf_link = div_pdf.a['href']
                            pdf_izena = pdf_link.split('/')[-1]
                            self._refs.append({'link': pdf_link, 'pdf_name': pdf_izena})

                        pdf.append(uria)

                progress += 1.5
                progress_var.set(progress)
                progress_bar.update()
                time.sleep(0.1)

            section = section + 1

        popup.destroy()
        return self._refs


    def get_pdf(self, selection):
        print("##### PDF-a deskargatzen... #####")
        metodoa = 'GET'
        print("Metodoa: ")
        print(metodoa)
        uria = self._refs[selection]['link']
        print("Uria: ")
        print(uria)
       # headers = {'Host': 'egela.ehu.eus',          'Cookie': self._cookiea}
        erantzuna = requests.get(uria, allow_redirects=False)
        pdf_file = erantzuna.content
        pdf_name = self._refs[selection]['pdf_name']
        print("PDF Izena: ")
        print(pdf_name)

        return pdf_name, pdf_file
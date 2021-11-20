import urllib

import pdfkit
import requests
from bs4 import BeautifulSoup
import weasyprint

def html2pdf(url):
    pdfname=url.replace('http:://','D')
    pdfname = pdfname.replace('https://', 'D')
    pdfname = pdfname.replace('/', '-')

    doc_pdf = weasyprint.HTML(url).write_pdf(pdfname)

    #pdfname=pdfname.concat('.pdf')
    #config_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    #config = pdfkit.configuration(wkhtmltopdf=bytes("/usr/local/bin/wkhtmltopdf", 'utf8'))
   # pdfkit.from_url('url', pdfname+'.pdf',configuration=config_path)

def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

def getAllLinks(url):
    lista=[]
    datos = urllib.request.urlopen(url).read().decode()
    soup = BeautifulSoup(datos)
    tags = soup('a')
    for tag in tags:
        if is_downloadable(tag.get('href')):
            lista.append(tag.get('href'))
    return lista


def download(url):
    pdfname = url.replace('http:://', '')
    pdfname = pdfname.replace('https://', '')
    pdfname = pdfname.replace('/', '-')
    r = requests.get(url, allow_redirects=True)
    open(pdfname, 'wb').write(r.content)
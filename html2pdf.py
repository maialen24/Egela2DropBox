import pdfkit
import weasyprint

def html2Pdf(url,gorde):
    pdfName=url.replace('http','')
    pdfName = pdfName.replace('https', '')
    pdfName = pdfName.replace('/', '')

    pdfkit.from_url('https://www.google.co.in/', gorde+pdfName+'.pdf')


doc_pdf = weasyprint.HTML('https://www.delftstack.com/').write_pdf('sample.pdf')

#html2Pdf('https://www.delftstack.com/es/howto/python/html-to-pdf-python/','.')
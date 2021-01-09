import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Progressbar
import pdfrw
import pdfrw
import PyPDF4
from PyPDF4 import PdfFileWriter, PdfFileReader,PdfFileMerger
from tkinter import Tk, HORIZONTAL  # from tkinter import Tk for Python 3.x
from tkinter import filedialog as fd
from tkinter import messagebox

from fpdf import FPDF

gui = tkinter.Tk()
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# uploaded_file = askopenfilename()
uploaded_file = fd.askopenfilename()
# uploaded_file = "863573077_05-01-2021_12_2020_5.pdf"
x = pdfrw.PdfReader(uploaded_file)
y = pdfrw.PdfWriter()
y.addpages(x.pages)
y.write(uploaded_file)
pdf_writer = PdfFileWriter()
# pdf_writer = FPDF()

pdfFileObj = uploaded_file
pdfReader = PyPDF4.PdfFileReader(pdfFileObj)

totalpaginas = pdfReader.getNumPages()

#############

WIDTH = 210
HEIGHT = 297
pdf_background = FPDF()
pdf_background.add_page()
pdf_background.image("rect1.png", 10, 280, WIDTH - 50,HEIGHT-100)
pdf_background.output("rect.pdf", "F")
pdf_background = PdfFileReader(open("rect.pdf", "rb"))
pdf_background.getPage(0)




for i in range(totalpaginas):

    pageObj = pdfReader.getPage(i)
    teste = pageObj.extractText().split()
    contador1 = 0
    contador2 = 0

    for j in teste:
        if j == 'dinheiro.':
            p = pdfReader.getPage(i)
            #pdf_writer.addPage(p)
            #pdf_writer.getPage(0)
            page = pdf_background.getPage(0)
            page.mergePage(p)
            pdf_writer.addPage(page)

        if j =='detalhes':
            p = pdfReader.getPage(i)
            pdf_writer.addPage(p)
        if j == 'Tributos' and contador1 == 0:
            contador1 = 1
            p = pdfReader.getPage(i)
            pdf_writer.addPage(p)

        if j == 'Ressarcimento' and contador2 == 0:
            contador2 = 1
            p = pdfReader.getPage(i)
            pdf_writer.addPage(p)



#output = PdfFileWriter()


#page = rect.getPage(0)
#page.mergePage(input1.getPage(0))
#output.addPage(page)


# os.mkdir("C:\\conta_modificada")
with open("conta_modificada.pdf", 'wb') as f:
    pdf_writer.write(f)
    messagebox.showinfo("Aviso", "Conta corrigida e convertida para análise")




# finally, write "output" to document-output.pdf
#outputStream = open("document-output.pdf", "wb")
#output.write(outputStream)
#outputStream.close()

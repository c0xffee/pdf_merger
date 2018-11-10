import os
from PyPDF2 import PdfFileMerger

###pdfs = ['sth.pdf', 'id1.pdf', 'id2.pdf']
pdfs = os.listdir()

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

fname = input('filename:')    
    
merger.write(fname)
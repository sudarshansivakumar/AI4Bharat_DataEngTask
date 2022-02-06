# Performs OCR on all the images for each of the PDFs and stored the PDF text in a text file 
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
import pytesseract
from PyPDF2 import PdfFileReader
import fitz

start_idx = 1
end_idx = 48

for i in range(start_idx,end_idx) :
    out_file = "PDF" + str(i) + "/output.txt"
    f = open(out_file, "a",encoding = 'utf-8')

    pdf_file = "PDF" + str(i) + "/data.pdf"

    if(os.path.exists(pdf_file) == False) :
        print("PDF does not exist")
        continue
    try :
        myPdf = PdfFileReader(open(pdf_file,'rb'))
        num_pages = myPdf.getNumPages()
        print(f"Number of pages for PDF {i} = {num_pages}")

        for j in range(1, num_pages + 1):
            filename = "PDF" + str(i) +  "/page_"+ str(j) +".jpg"
            text = "----------------- " + "\n" + str((pytesseract.image_to_string(Image.open(filename),lang = 'hin')))
            text = text.replace('-\n', '') 
            f.write(text)
            print(f"Page {j} done in PDF {i}")
    except :
        print(f"Could not complete process for PDF {i}")
        continue
    f.close()

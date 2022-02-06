# Takes all of the saved PDFs, and converts each page of these PDFs into an image. This will help us with OCR that will then be performed 
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader
import fitz
import os

start_idx = 0
end_idx = 48
for i in range(start_idx,end_idx) :
    pdf_file = "PDF" + str(i) + "/data.pdf"
    if(os.path.exists(pdf_file) == False) :
        print("PDF does not exist")
        continue

    try :
        myPdf = PdfFileReader(open(pdf_file,'rb'))
        num_pages = myPdf.getNumPages()
        doc = fitz.open(pdf_file)
        for j in range(num_pages) :
            page = doc.loadPage(j)
            pix = page.get_pixmap()
            output_file = "PDF" + str(i) + "/" + "page_" + str(j + 1) + ".jpg"
            pix.save(output_file)
            print(f"Page {j + 1} saved in PDF {i}")
        print("------------------")
    except :
        print("Could not complete process for PDF {i}")
        continue



""""
PDF_file = "PDF" + str(i) + "/data.pdf"
pages = convert_from_path(PDF_file)
print(f"Converted PDF {i} from path")
image_counter = 1
for page in pages :
    filename = "PDF" + str(i) +  "/" +  "page_"+ str(image_counter)+".jpg"
    print(filename)
    page.save(filename, 'JPEG')
    image_counter = image_counter + 1
    print("------------")

"""

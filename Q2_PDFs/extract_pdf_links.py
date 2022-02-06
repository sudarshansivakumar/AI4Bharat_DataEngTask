# We have a list of URLs in "Marathi_URLs_2.csv" - some of these link to PDF files
# while others link to webpages which contain PDFs. This programme creates and saves a CSV file
# which contains all the PDF links in one file "Marathi_PDFs_final.csv"
import pandas as pd 
import numpy as np 
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
import re
import requests
from bs4 import BeautifulSoup

def get_pdf_from_URL(link) :
    # This takes a webpage as input and finds the link which directs to a PDF file. This is done by using the Beautiful Soup 
    # find_all function followed by a search for the substring PDF in the html text (This works because the archive.org links)
    # had the text PDF associated with each PDF hyperlink
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    allLinks = soup.find_all("a")
    for link in allLinks :
        if("PDF" in link.text) :
            if (re.search('.pdf$', link['href']) != None) :
                return link['href']
    return None

def get_pdf_links(path = 'Marathi_URLs_2.csv') : 
    df = pd.read_csv(path)
    pdf_links = list()
    pdf_ext = ".pdf"

    for link in df['URLs'].values :
        isPdf = re.search('.pdf$', link)
        if(isPdf != None) :
            print(link)
            pdf_links.append(link)
        else :
            isSlideShow = re.search('\?view=theater$',link)
            if(isSlideShow != None) :
                x = "?view=theater"
                link = link[ : -len(x)]
            pdf_link_back = get_pdf_from_URL(link)

            if(pdf_link_back != None) :
                pdf_link = "https://archive.org" + pdf_link_back
                print(pdf_link)
                pdf_links.append(pdf_link)

    print(len(pdf_links))
    print(len(df['URLs'].values))
    return pdf_links
    
pdf_links = get_pdf_links()

pdf_links.append("https://archive.org/download/dli.ministry.31030/13277.8861%2520%2528part-1%2529.pdf")
pdf_links.append("https://archive.org/download/dli.ministry.31030/13277.8861%2520%2528part-2%2529.pdf")
pdf_links.append("https://archive.org/download/dli.ministry.31030/13277.8861%2520%2528part-3%2529.pdf")

df = pd.DataFrame({'URLs' : pdf_links})
df.to_csv("Marathi_PDFs_final.csv")
print(df)
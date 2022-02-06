# Creates a CSV file with all the URLs using the link given in the sheet 

from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd
import numpy as np
import csv

def create_csv(sheets_url) : 
    sheet_html = requests.get(sheets_url).text
    soup = BeautifulSoup(sheet_html, "html.parser")
    table = soup.find("table")
    index = 0
    with open("Marathi_URLs" + ".csv", "w") as f:
        wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        wr.writerows([[td.text for td in row.find_all("td")] for row in table.find_all("tr")])
        index = index + 1

sheets_url = 'https://docs.google.com/spreadsheets/d/1I7hziCQGd0uKzh4RMnZtpkTspaE-1_bIL0FcGU_Y1DU/edit#gid=1169510777'
create_csv(sheets_url)
print("Created a CSV with all the URLs")
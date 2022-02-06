# We locally store each of the PDF links present in Marathi_PDFs_final.csv
from pathlib import Path
import requests
import pandas as pd
import os 

df = pd.read_csv('Marathi_PDFs_final.csv')
idx = 46
for link in df['URLs'].values[idx - 1 :] :
    directory_name = "PDF" + str(idx)
    if(os.path.isdir(directory_name) == False) :
        os.mkdir(directory_name)
    file_path = directory_name + "/data.pdf"
    filename = Path(file_path)
    response = requests.get(link)
    filename.write_bytes(response.content)
    print(link)
    idx += 1

print("All PDFs have been saved")






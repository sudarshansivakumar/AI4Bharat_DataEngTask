import json 
import pandas as pd
import os


dict_list = list()
df_page_urls = pd.read_csv("Marathi_URLs_2.csv")
df_pdf_urls = pd.read_csv("Marathi_PDFs_final.csv")
page_urls = df_page_urls['URLs'].values
pdf_urls = df_pdf_urls['URLs'].values

for i in range(0,48) :    
    if( i <= 22) :
        pdf_content_path = "PDF" + str(i + 1) + "/output.txt"
    else :
        pdf_content_path = "output" + str(i + 1) + ".txt"
    if(os.path.exists(pdf_content_path)) :
            with open(pdf_content_path,"r",encoding = 'utf-8') as f :
                data = f.read()
    else :
        print(f"PDF {i + 1} does not have any data")
        data = ""
    my_dict = {
                "page-url"  : page_urls[i],
                "pdf-url"  : pdf_urls[i],
                "pdf-content" : data
              }
    dict_list.append(my_dict)
    print(f"PDF {i + 1} done")

output_file_name = "pdf_output.json"
with open(output_file_name,'w',encoding = 'utf-8') as fout :
    json.dump(dict_list,fout,ensure_ascii= False)
#print(dict_list[0])
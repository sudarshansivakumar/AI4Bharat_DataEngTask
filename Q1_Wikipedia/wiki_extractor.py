import argparse
import sys
import numpy as np
from bs4 import BeautifulSoup 
import requests
import nltk
import wikipedia 
import json


def get_page_name(url_back) :
    page_name = "" 
    idx = 0
    for character in url_back[6:] :
        if(character == '_') :
            page_name = page_name + " "
        else :
            page_name = page_name + character
    return page_name

def get_paragraph(p) :
    paragraph = ""
    for character in p : 
        paragraph = paragraph + character
        if(character == '\n') :
            break
    return paragraph
parser = argparse.ArgumentParser(description= 'Extract keyword, number of files, and output file name')
parser.add_argument('--keyword', help='Wikipedia search term')
parser.add_argument('--num_urls', help='The number of URLs we are supposed to save in json file')
parser.add_argument('--output',help='Name of output json file')

args = parser.parse_args()

if args.keyword :
    print(f"Keyword : {args.keyword}")

if args.num_urls :
    print(f"Number of URLs : {args.num_urls}")

if args.output :
    print(f"Output File Name : {args.output}")

search_term = args.keyword
n = args.num_urls
output_file_name = args.output
search_term_words = search_term.split()

search_words_comb = ""
for word in search_term_words :
    search_words_comb += word + "+"
    
search_words_comb = search_words_comb[:-1]

url_parts = list()
url_parts.append("https://en.wikipedia.org/w/index.php?title=Special:Search")
url_parts.append("limit=" + str(n))
url_parts.append("offset=0")
url_parts.append("profile=default")
url_parts.append("search=" + search_words_comb)
url_parts.append("ns0=1")

search_url = ""
for url_part in url_parts :
    search_url += url_part + "&"
search_url = search_url[:-1]

print(f"Search URL : {search_url}")
r = requests.get(search_url)
soup = BeautifulSoup(r.content, 'html.parser')
allLinks = soup.select(".mw-search-result-heading a")

related_pages = list()
related_pages_names = list()
for link in allLinks :
    
    url_back = link.get('href') #/wiki/Historical_events_of
    tag_class = link.get('class')
    #print(f"Class :{tag_class}")
    if ((tag_class != None ) and (tag_class[0] == 'mw-redirect')):
        continue
    #print(link)
    page_name = get_page_name(url_back)
    related_page_url = "https://en.wikipedia.org" + url_back
    related_pages.append(related_page_url)
    related_pages_names.append(page_name)
    print(related_page_url)
    print(page_name)
"""
url2 = related_pages[0]
r = requests.get(url2)
soup2 = BeautifulSoup(r.content, 'html.parser')
allParagraphs = soup.select("#mw-content-text > div.mw-parser-output > p:nth-child(9)")
print(allParagraphs)
#print(f"URL Heading : {allLinks}")
"""
page_paragraphs = list()
for page in  related_pages_names :
    #print(page)
    p = wikipedia.summary(page,auto_suggest = False)
    paragraph = get_paragraph(p)
    page_paragraphs.append(paragraph)

# related_pages has the urls of all the relevant pages
# page_paragraphs has all the paragraph descriptions of these pages
# related_pages_names has the names of the pages
dict_list = list()
for idx in range(len(related_pages)) :
    url = related_pages[idx]
    paragraph = page_paragraphs[idx]
    mydict = {"url" : url, "paragraph" : paragraph}
    dict_list.append(mydict)

print(f"Length of dictionary list : {len(dict_list)} ")

with open(output_file_name,'w') as fout :
    json.dump(dict_list,fout)

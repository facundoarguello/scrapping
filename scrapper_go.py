from os import path, linesep
from pathlib import PurePath
from bs4 import BeautifulSoup
import requests
from datetime import datetime


try:
    response = requests.get("https://news.google.com/search?q=lisandro+martinez")
    if response.ok:
        text = response.text
except requests.exceptions.ConnectionError as exc:
    print(exc)

html = BeautifulSoup(text, 'html.parser')
article_header = html.find(class_='article-header')
# f = open("exx.html", "w")
# f.write(str(html))
# f.close()
            
list_notes = html.find_all("div", class_='NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc')

# list_notes = list_notes.find_all('div', class_='Gx5Zad fP1Qef xpd EtOod pkphOe')

f = open("gool.html", "w")
f.write(str(list_notes))
f.close()

# print(list_notes[0]find_all('a'))
# arr = []
# for x in list_notes:
#     row = {}
#     row['href'] = x.find_all('a')[0]['href']
#     arr.append(row)
# print(arr)


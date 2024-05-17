from os import path, linesep, mkdir, remove , rmdir
from pathlib import PurePath
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from shutil import rmtree
import json

print("="*10,"COMIENZO DEL SCRAP", "="*10)

# url = 'https://www.espn.com.ar/futbol/argentina/nota/_/id/11895086/boca-juniors-almiron-defensores-reserva-bajas-entrenamiento'
# try:
#     response = requests.get(url)
#     if response.ok:
#         text = response.text
# except requests.exceptions.ConnectionError as exc:
#     print(exc)



# html = BeautifulSoup(text, 'html.parser')
   
# article_header = html.find(class_='article-header')
# title = article_header.find_all('h1')[0].string

# article_body = html.find(class_='article-body')
# p_arr = article_body.find_all('p')

# asides = article_body.find_all('aside')[0]
# source = asides.find_all('source')[0]

# img = source['data-srcset'].split(',')[0]

# article_meta = html.find(class_="article-meta")

# autor_name = article_meta.find(class_='author').get_text()
# date_time = article_meta.find(class_='timestamp')['data-date']


# text_ret = ""
# for x in p_arr:
#     text_ret += ' ' + x.get_text()



# results = text['results']
# results_article = []
# content = []
# if len(results) > 0: 
#     results_article = [ x for x in results if x['type'] == 'article' ]
#     if len(results_article) > 0: 
#         content = results_article[0]['contents']


# for j in content:
#     title = j['displayName']
#     href = j['link']['web']
#     print(title)
#     if 'images' in j:
#         img = j['images'][0]['url']
#     else : 
#         img = ''
                


# Obtiene la hora actual
now = datetime.now()

# Crea un objeto datetime para representar 2 horas antes


# Formatea la hora resultante en el formato deseado
# formatted_date = two_hours_ago.strftime('%Y-%m-%d %H:%M:%S')
url = 'https://www.espn.com.ar/'


try:
    response = requests.get(url)
    if response.ok:
        text = response.text
except requests.exceptions.ConnectionError as exc:
    print(exc)
arr_ole = []

html = BeautifulSoup(text, 'html.parser')
news_feed= html.find(id='news-feed')

a_etiqta_ar = news_feed.find_all('a')
index = 0


for x in a_etiqta_ar:
    title_wrapper = x.find_all('div', class_='contentItem__titleWrapper')
    if len(title_wrapper) >0 :
        title = title_wrapper[0].find_all('h1')[0].get_text()
        href = 'https://www.espn.com.ar'+x['href']
        img = x.find_all('img')[0]['data-default-src']
        time_str = x.find(class_='contentMeta__timestamp').get_text()
        


        if 'm' in time_str:
            parts = time_str.split('m')
            num = int(parts[0])
            calculated_date = now - timedelta(minutes=num)
            formatted_date = calculated_date.strftime('%Y-%m-%d %H:%M:%S')
            
        if 'h' in time_str:
            parts = time_str.split('h')
            num = int(parts[0])
            calculated_date = now - timedelta(hours=num)
            formatted_date = calculated_date.strftime('%Y-%m-%d %H:%M:%S')
            
        if 'd' in time_str:
            parts = time_str.split('d')
            num = int(parts[0])
            calculated_date = now - timedelta(days=num)
            formatted_date = calculated_date.strftime('%Y-%m-%d %H:%M:%S')
            
       



f = open("espn.html", "w")
f.write(str(text_ret))
f.close()



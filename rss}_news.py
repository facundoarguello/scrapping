from os import path, linesep
from pathlib import PurePath
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import feedparser

# parser = feedparser.parse('https://news.google.com/rss/search?q=belgrano+Cordoba&hl=es-419&gl=AR&ceidAR:es&ceid=AR:es-419')
# entries = parser['entries']
# indice = 0
# entries = sorted(entries, key=lambda item: item['published_parsed'], reverse=True)
# # print(entries)
# for x in entries:
#     url = x['source']['url']
#     author = x['source']['title']
#     # print(x['title_detail'])
#     # print(x['pubDate'])
#     print(x['published'])
#     try:
#         response = requests.get(x['link'])
#         if response.ok:
#             text = response.text
#     except requests.exceptions.ConnectionError as exc:
#         print(exc)

    
#     html = BeautifulSoup(text, 'html.parser')

#     head = html.find('head')
#     url_clean = head.find('link', {'rel': 'canonical'})
#     logo_tag = head.find('link', {'rel': 'icon'})
#     # print(logo_tag)
#     img_meta = head.find('meta',{'property':'og:image'})
#     if logo_tag != None and img_meta!= None and url_clean !=None:

#         url_clean = url_clean['href']
#         # print(url_clean)
#         logo_url = logo_tag['href']
#         if 'http' not in logo_url:
#             if logo_tag['rel'] ==['shortcut','icon']:
#                 logo_url = url + logo_tag['href']
#         if logo_url == '/favicon.ico' or logo_url== '/images/icons/favicon.png' or logo_url== '/images/icons/favicon.ico':
#             logo_url = url + logo_url
   

#         img = img_meta['content']
#         # print(img)
#         indice += 1
#         if indice == 10 :
#             break
        

# f = open("rss_g.html", "w")
# f.write(str(head))
# f.close()
format_date = '%Y-%m-%d %H:%M:%S'
split = 'VfL Wolfsburg'.split()
join_name = "+".join(split)

parser = feedparser.parse(f'https://news.google.com/rss/search?q={join_name}+-site:ole.com.ar&hl=es-419&gl=AR&ceidAR:es&ceid=AR:es-419')
entries = parser['entries']
entries = sorted(entries, key=lambda item: item['published_parsed'], reverse=True)

# print("key:",key, "position:", pos)
# print(entries)
index = 0
limit = 1
for j in entries:
    url = j['source']['url']
    author = j['source']['title']
    # Fecha en formato original
    fecha_original = j['published']

    # Convierte la fecha original a un objeto datetime
    fecha_datetime = datetime.strptime(fecha_original, '%a, %d %b %Y %H:%M:%S %Z')

    # Convierte la fecha datetime a un string con el formato deseado
    fecha_formateada = fecha_datetime.strftime(format_date)

    text = None

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(j['link'], headers=headers)
        if response.ok:
            text = response.text
      
    except requests.exceptions.ConnectionError as exc:
        print(exc)
    
    if text != None:
        html = BeautifulSoup(text, 'html.parser')

        head = html.find('head')
        f = open("prueba.html", "w")
        f.write(str(html))
        f.close()
        url_clean = head.find('link', {'rel': 'canonical'})
        logo_tag = head.find('link', {'rel': 'icon'})
        img_meta = head.find('meta',{'property':'og:image'})
        if logo_tag != None and img_meta!= None and url_clean != None:
            url_clean = url_clean['href']
            logo_url = logo_tag['href']
            if 'http' not in logo_url:
                if logo_tag['rel'] ==['shortcut','icon']:
                    logo_url = url + logo_tag['href']
            if logo_url == '/favicon.ico' or logo_url== '/images/icons/favicon.png' or logo_url== '/images/icons/favicon.ico':
                logo_url = url + logo_url

            img = img_meta['content']
            index += 1
            print("logo", logo_url)
            print("img", img)
            print(index)
            if limit == index:

                break
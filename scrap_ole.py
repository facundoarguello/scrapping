from os import path, linesep, mkdir, remove , rmdir
from pathlib import PurePath
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from shutil import rmtree

print("="*10,"COMIENZO DEL SCRAP", "="*10)

url = 'https://www.ole.com.ar/futbol-primera'
url_ole = 'https://www.ole.com.ar'
with open('url.txt', 'r') as fh:
    urls = fh.readlines()
urls = [url.strip() for url in urls]  # strip `\n`


arr = []
path_local = f'./ole_{datetime.now().strftime("%Y-%m-%d")}'
for url in urls:
    file_name = PurePath(url).name
    mkdir(f"{path_local}")
    file_path = path.join(f'{path_local}', file_name)
    text = ''

    try:
        response = requests.get(url)
        if response.ok:
            text = response.text
    except requests.exceptions.ConnectionError as exc:
        print(exc)
    
    with open(file_path, 'w') as fh:
        fh.write(text)

    arr.append(file_path)

arr_urls_teams = []
for i in arr:
    print(i)
    text = open(i).read()
    html = BeautifulSoup(text, 'html.parser')
    tira_header = html.find_all('div', {"class": "tira-header"})
    lista_equipos = tira_header[0].ul
    for x in lista_equipos:
        arr_urls_teams.append(x.a.get('href'))

mkdir(f"{path_local}/teams")
arr_url_notices = []
arr_2 = []
for url in arr_urls_teams:
    file_name = PurePath(url).name
    
    mkdir(f'{path_local}/teams/{file_name}')
    file_path = path.join(f'{path_local}/teams/{file_name}', file_name)
    text = ''

    try:
        response = requests.get(url)
        if response.ok:
            text = response.text
    except requests.exceptions.ConnectionError as exc:
        print(exc)
    
    with open(file_path, 'w') as fh:
        fh.write(text)

    arr_2.append(file_path)

for x in arr_2:
    text = open(x).read()
    
    html = BeautifulSoup(text, 'html.parser')
    undefined_class = html.find_all('div', {"class": "undefined"})
    try:
        list_noticees = undefined_class[0].ul
    except:
        list_noticees = []
    for x in list_noticees:
        # print(x.a.get('href'))
        arr_url_notices.append(f'{url_ole}{x.a.get("href")}')
       
        
# print(arr_url_notices)
mkdir(f'{path_local}/notices')
for url in arr_url_notices:
    file_name = PurePath(url).name
    file_path = path.join(f'{path_local}/notices', file_name)
    text = ''

    try:
        response = requests.get(url)
        if response.ok:
            text = response.text
    except requests.exceptions.ConnectionError as exc:
        print(exc)
    
    with open(file_path, 'w') as fh:
        fh.write(text)

    arr_2.append(file_path)


arr_return_body = []

for i in arr_2:
    try:
        text = open(i).read()
        html = BeautifulSoup(text, 'html.parser')
        # print(2)
        story_body= html.find(id='storyBody')
        # print(3)
        text_ret = "" 
        for x in story_body:
            if x.get('class') == ['custom-text']:
                p = x.find_all('p')
                if len(p) > 0:
                    text_ret += ' ' + p[0].get_text()
        arr_return_body.append(text_ret)
    except :
        pass

# print(arr_return_body[0])
try:
    mkdir(f'./return/{datetime.now().strftime("%Y-%m-%d")}')
except:
    pass
arr_py = open(f"./return/{datetime.now().strftime('%Y-%m-%d')}/arr_data_{datetime.now()}.py", "w")
arr_py.write(f"body_list ={arr_return_body}")
rmtree(f'{path_local}')


data_txt = open(f"./return/{datetime.now().strftime('%Y-%m-%d')}/data_{datetime.now()}.txt", "w")


for item in arr_return_body:
    data_txt.write("%s\n" % item)







    



    




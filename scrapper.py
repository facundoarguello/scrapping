from os import path, linesep
from pathlib import PurePath
from bs4 import BeautifulSoup
import requests
from datetime import datetime


def get_content(url):

    headers = {'Content-Type': 'application/json;charset=UTF-8', 'Access-Control-Allow-Origin': '*'}
    content = None

    # Get content
    r = requests.get(url, headers=headers)

    # Decode JSON response into a Python dict:
    content = r.json()

    return content


data = get_content("https://www.ole.com.ar/api/lomasleidos/all")['data']
urls = open("urls.txt", "w")
for x in data:
    urls.write("https://www.ole.com.ar" + x['url'] + linesep)

urls.close()
with open('urls.txt', 'r') as fh:
    urls = fh.readlines()
urls = [url.strip() for url in urls]  # strip `\n`


arr = []
for url in urls:
    file_name = PurePath(url).name
    file_path = path.join('.', file_name)
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

arr_return_body = []
for i in arr:
    text = open(i).read()
    html = BeautifulSoup(text, 'html.parser')

    story_body= html.find(id='storyBody')

    text_ret = "" 
    for x in story_body:
        
           
        if x.get('class') == ['custom-text']:
            p = x.find_all('p')

            if len(p) > 0:
                text_ret += p[0].get_text()
    arr_return_body.append(text_ret)

print(arr_return_body[0])

arr_py = open(f"arr_data_{datetime.now()}.py", "w")
arr_py.write(f"body_list ={arr_return_body}")


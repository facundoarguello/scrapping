from os import path, linesep, mkdir, remove , rmdir
from pathlib import PurePath
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from shutil import rmtree
import json

print("="*10,"COMIENZO DEL SCRAP", "="*10)

now = datetime.now()


url = 'https://www.promiedos.com.ar/primera'

img_url = 'https://www.promiedos.com.ar/'

arr = []

try:
    response = requests.get(url)
    if response.ok:
        text = response.text
except requests.exceptions.ConnectionError as exc:
    print(exc)
arr_ole = []

html = BeautifulSoup(text, 'html.parser')

div = html.find('div', {'id': 'tablaseccion'})
tbody = div.find('tbody')



arr_trs = div.find_all('tr')
arr_de_arrs = []
for x in arr_trs:
    row = {}
    tds_arr = x.find_all('td')
    if len(tds_arr) == 0:
         tds_arr = x.find_all('th')
    arr_datos = []
    for j in tds_arr:
        img_com = j.find('img')
        if img_com != None:
            obj = {
                "img": img_url + img_com['src'],
                "name" : j.get_text()
            }
            arr_datos.append(obj)
        else:
            arr_datos.append(j.get_text())

    arr_de_arrs.append(arr_datos)



keys = arr_de_arrs[0]


result = []

for values in arr_de_arrs[1:]: # itera sobre los valores desde el segundo arreglo hasta el último
    dic = {}
    for i, value in enumerate(values):
        dic[keys[i]] = value # si el valor no es un diccionario, lo agrega como valor del diccionario con la key correspondiente
    result.append(dic)



f = open("promiedos", "w")
f.write(str(result))
f.close()




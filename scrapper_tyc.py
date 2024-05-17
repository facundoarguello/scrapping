from os import path, linesep, mkdir, remove , rmdir
from pathlib import PurePath
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from shutil import rmtree
import json

print("="*10,"COMIENZO DEL SCRAP", "="*10)

# url = 'https://www.tycsports.com/boca-juniors/rafa-di-zeo-mauro-martin-barra-boca-poder-politico-escuchas-telefonicas-id504486.html'
url = 'https://ks0ox7o92c.execute-api.us-east-1.amazonaws.com/PROD/search?q=Barcelona&size=5&start=0&sort=publicado%20desc'


try:
    response = requests.get(url)
    if response.ok:
        text = json.loads(response.text)
except requests.exceptions.ConnectionError as exc:
    print(exc)



hits = text['hits']['hit']
for j in hits:
                
    fields = j['fields']
    titulo = fields['titulo']
    publicado = fields['publicado']
    href = fields['url']
    con_json = json.loads(fields['con_json'][0])
 
    
    con_multimedia = con_json['multimedia']
    if len(con_multimedia) > 0: 
        con_multimedia = con_json['multimedia'][0]
        items_multimedia = con_multimedia['items_multimedia'][0]
        imagen = items_multimedia['imagen']
    else:
        con_imagen = json.loads(con_json['con_imagen'])
        imagen = con_imagen['imagen']
    

    imagen = imagen.replace('.jpg','')

    img =f'https://media.tycsports.com/{imagen}_416x234.webp'



# con_json['con_imagen'] = json.loads(con_json['con_imagen'])




# print(text)





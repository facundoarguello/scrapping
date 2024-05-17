from os import path, linesep, mkdir, remove , rmdir
from pathlib import PurePath
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from shutil import rmtree
import json

print("="*10,"COMIENZO DEL SCRAP", "="*10)

url = 'https://www.hoysejuega.com/listado-torneos.htm'


try:
    response = requests.get(url)
    if response.ok:
        text = response.text
except requests.exceptions.ConnectionError as exc:
    print(exc)

html = BeautifulSoup(text, 'html.parser')
# list_torneos_destacados = html.find_all('a', {"class": "Listado torneos"})
class_gris_pages = html.find('td', {"class": "gris"})
list_pages = class_gris_pages.find_all('a')
f = open("torneo_emilio", "a")
for page in list_pages:
    list_info_torneos = []
    print("number_page", page.string)
    if page.string not in ('Siguiente','1','2','3','4','5','6','7','8','9', '10', '11','12','13','14','15','16','17', '18', '19', '20','21','22','23','24'):
        url_page = page['href']
        print("url_page:",url_page)
        try:
            response_page = requests.get(url_page)
            if response_page.ok:
                individual_page = response_page.text

        except Exception as exc:
            print(exc)
            continue
        
        html_page = BeautifulSoup(individual_page, 'html.parser')
        list_torneos_destacados = html_page.find_all('ul', {"class": "torneos_destacados"})
        print(len(list_torneos_destacados))
        
        for torneo in list_torneos_destacados:
            objeto_torneo = {}
            objeto_torneo['url'] = None
            objeto_torneo['tipo'] = None
            objeto_torneo['descripcion'] = None
            objeto_torneo['servicios'] = None
            objeto_torneo['datos_contacto'] = None
            objeto_torneo['sede'] = None


            href_only_tournament = torneo('a')
            url_torneo = href_only_tournament[0]['href']
            try:
                print("url_torneo", url_torneo)
                response_tor = requests.get(url_torneo)
                if response_tor.ok:
                    torneo_page_html = response_tor.text

            except Exception as exc:
                print(exc)
                continue

            html_page_tour = BeautifulSoup(torneo_page_html, 'html.parser')
            info_cancha = html_page_tour.find('div', id='infoCancha2')
            if info_cancha is None :
                continue
            url_torneo_page = info_cancha.find('a', {"class": "verde7 underline"})
            objeto_torneo['url'] = None
            print(url_torneo_page)
            if url_torneo_page:
                if 'href' in url_torneo_page:
                    objeto_torneo['url'] = url_torneo_page['href']

            find_descripcion_tipo_servicios = info_cancha.find_all('p',{"class": "negro txt12"})
            for paraghrap in find_descripcion_tipo_servicios:
                # print(paraghrap)
                strongs = paraghrap('strong')
                print(strongs)
                if len(strongs) > 0 and strongs[0].string == 'JUGADORES:':
                    br = paraghrap.text
                    # print(br)
                    objeto_torneo['tipo'] = br
                if len(strongs) > 0 and strongs[0].string == 'DESCRIPCIÓN:':
                    br = paraghrap.text
                    # print(br)
                    objeto_torneo['descripcion'] = br
                if len(strongs) > 0 and strongs[0].string == 'SERVICIOS:':
                    br = paraghrap.text
                    # print(br)
                    objeto_torneo['servicios'] = br
            
            telefono_find = info_cancha.find('p',{"class": "txt14"})
            # print(telefono_find.text)
            if telefono_find:
                objeto_torneo['datos_contacto'] = telefono_find.text
            sede_find = info_cancha.find('p',{"class": "verde2 txt13 bold"})
            # print(sede_find.text)
            if sede_find:
                objeto_torneo['sede'] = sede_find.text
            list_info_torneos.append(objeto_torneo)
    
            f.write(str(objeto_torneo)+ ',')
f.close()
print(list_info_torneos)
        #     break

        # break
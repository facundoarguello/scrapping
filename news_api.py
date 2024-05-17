import requests

# URL de la API de NewsAPI
url = "https://newsapi.org/v2/top-headlines"

# Parámetros de la solicitud para la búsqueda de noticias de fútbol
query_params = {
    "q": "fútbol",
    "category": "sports",
    "country": "ar",
    "pageSize": 1,
    "apiKey": "+++++"
}

# Realizar la solicitud GET a la API con los parámetros y obtener la respuesta
response = requests.get(url, params=query_params)

# Analizar los datos JSON de la respuesta
data = response.json()

# Imprimir los títulos y enlaces de las noticias
for article in data["articles"]:
    print(article)

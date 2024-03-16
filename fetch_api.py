import requests

base_url = 'https://aves.ninjas.cl/api/birds'

#Funcion que retorna los pajaros que vienen en el request a la API
def get_birds_data():
    return requests.get(base_url).json()
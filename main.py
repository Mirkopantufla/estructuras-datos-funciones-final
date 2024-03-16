from fetch_api import get_birds_data
from create_card import createCards
from create_html import createHTML

birds_data = get_birds_data() #Guardo lista de pajaros
cards = createCards(birds_data) #Creo las cartas
createHTML(cards) #Genero el HTML

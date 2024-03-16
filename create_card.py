
#Funcion para generar las cartas por cada pajaro presente en la lista pasada por parametros
def createCards(birdsData):
    card_template = ''

    for bird in birdsData:
        #Guardo en diferentes variables por cada iteracion de birdsData
        api_order = bird['sort'] #Dato adicional para complementar
        name = bird['name'] #Almacena el diccionario de nombres para utilizarlos todos
        image_link = bird['images']['full'] #Almacena la imagen de tamaño full

        #Por cada iteracion, se agrega a card_template, al final del ciclo entregara todas las cards generadas
        card_template += f'''
            <div class="card mb-3" style="max-width: 540px;">
                <div class="row g-0">
                    <div class="col-md-4">
                        <img src="{image_link}" class="img-fluid rounded-start" alt={name['latin']}>
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h5 class="card-title text-center">{name['latin']}</h5>
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item"><p class="card-text">En español: {name['spanish']}</p></li>
                                <li class="list-group-item"><p class="card-text">En ingles: {name['english']}</p></li>
                            </ul>
                            <small class="text-body-secondary text-center">Register N°{api_order}</small>
                        </div>
                    </div>
                </div>
            </div>
            '''
    
    return card_template


#Funcion que contiene el esqueleto del html, se insertan las cartas por parametro
#Todo se maneja en main.py
def createHTML(cards):

    HTML_template = f'''
    <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Bootstrap demo</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        <body>
            <div class='container'>
                <h1 class='text-center'>Pajaros Chilenos</h1>
                <div class='row d-flex justify-content-center justify-content-xl-between'>
                    {cards}
                </div>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </body>
    </html>
    '''

    #Genero el HTML si no existe. Si existe, modifica el existente.
    #Codificacion apropiada para caracteres en español
    index = open('index.html','w+',encoding='utf-8')
    index.write(HTML_template)
    

#    Compare_Nite by Mario Santamaría Osorio.
#    --------------------------------------
#      Copyright © RGBlines.sytes.net 2018
#    --------------------------------------
#    If you were to use this code you should
#             first ask the owner.

import requests
from flask import Flask, render_template, request

URL = 'https://api.fortnitetracker.com/v1/profile/pc/{}'

#Diccionario con datos de la api para acceder facilmente a ellos
headers = {'TRN-Api-Key' : '57e6a8ad-8fc9-4189-9fa6-6ac46a095231'}
#res = requests.get(URL, headers=headers)
#result = res.json()['lifeTimeStats']
app = Flask(__name__)


@app.errorhandler(500)
def page_not_found(e):
    # Carguemas el template si salta un error del servidor
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])#Metodos que acepta nuestra app
def index():
    player_one = None
    player_two = None
    player_one_stats = {}
    player_two_stats = {}

    #Si el metodo que recibe es POST...
    if request.method == 'POST':

        player_one = request.form.get('playerName')

        #Si existe el player_one nos preparamos para pillar un player_two
        if player_one:
            player_two = request.form.get('playerName')
        else:
            player_one = request.form.get('playerName')

        player_one_result = requests.get(URL.format(player_one), headers=headers).json()['lifeTimeStats']
        player_one_stats = populate_player_data(player_one_result)

        if player_two:
            player_two_result = requests.get(URL.format(player_two), headers=headers).json()['lifeTimeStats']
            player_two_stats = populate_player_data(player_two_result)

    return render_template('index.html', player_one=player_one, player_two=player_two,
        player_one_stats=player_one_stats, player_two_stats=player_two_stats)

#Funcion de obtencion de datos
def populate_player_data(api_data):

    temporary_dict = {}
    
    #La api nos da los datos en un json que llama a los valores de la siguiente forma -->

    #'Key: wins; 
    #    valores...'

    #Para cada key añadimos los valores al diccionario temporal

    for r in api_data:
        if r['key'] == 'Wins':
            temporary_dict['wins'] = r['value']

        if r['key'] == 'Kills':
            temporary_dict['kills'] = r['value']

        if r['key'] == 'Matches Played':
            temporary_dict['matches'] = r['value']
        #Datos box 2
        if r['key'] == 'Time Played':
            temporary_dict['time'] = r['value']

        if r['key'] == 'Avg Survival Time':
            temporary_dict['avg'] = r['value']

        if r['key'] == 'Score':
            temporary_dict['score'] = r['value']

    #Recogemos los valores
    return (temporary_dict)

#print (populate_player_data(result)). Esto lo usamos al principio para ver como nos da los datos la API

if __name__ == '__main__':
    app.run(debug=False, port=3260, host='x.x.x.x') #Añade el host donde corre la app

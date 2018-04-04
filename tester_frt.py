import requests
from flask import Flask, request

URL = 'https://api.fortnitetracker.com/v1/profile/pc/Twitch_Svennoss'

#Diccionario con datos de la api para acceder
headers = {'TRN-Api-Key' : '57e6a8ad-8fc9-4189-9fa6-6ac46a095231'}

res = requests.get(URL, headers=headers)

print (res.text)

# Dado que la API no tiene demasiada información sobre su uso,
# tenemos que ver primero como nos va a dar los datos.
#--------------------------------------------------------------------------------
# Para ello, haremos na petición al servidor pidiendole los headers (datos) 
# de un jugador, en este caso hardcodeamos el jugador en la URL para hacer pruebas.

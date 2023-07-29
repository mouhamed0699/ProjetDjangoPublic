from django.test import TestCase
import json
# Create your tests here.
import requests

access_key = '06f4597a679d37f660f8ca00fc816ec2'
airport_name = 'Aéroport de Paris-Charles-de-Gaulle'

url = f'http://api.aviationstack.com/v1/airlines?access_key={access_key}&airport_name={airport_name}'

response = requests.get(url)
if response.status_code == 200:
    # Convertir la réponse JSON en un objet Python
    data = response.json()

    # Enregistrer les données dans un fichier JSON
    with open('data.json', 'w') as file:
        json.dump(data, file)

    print("Les données ont été enregistrées dans le fichier data.json.")
else:
    print("La requête n'a pas abouti avec succès.")

import requests


request = requests.get('https://pokeapi.co/api/v2/pokemon-species/','limit=1000')
data = request.json()['results']
for pokemon in data:
    print (pokemon['name'])
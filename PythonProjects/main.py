import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fc89232c8210f6aee76fd3a6349d1fcd'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

POKEMON_ID = response_create.json()['id']

body_rename = {
	
    "pokemon_id": POKEMON_ID,
    "name": "New Name"

}
response_rename = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)

body_add_pokeball = {
    "pokemon_id": POKEMON_ID
}

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

body_knockout = {
    "pokemon_id": POKEMON_ID
}
response_knockout = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = body_knockout)
print(response_knockout.text)

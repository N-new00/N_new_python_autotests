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

body_rename = {
	
    "pokemon_id": "172371",
    "name": "New Name"

}
response_rename = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)

body_add_pokeball = {
    "pokemon_id": "172371"
}

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

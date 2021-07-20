import requests, json
url = "https://pokeapi.co/api/v2/"  
response = requests.get(url)
if not response.ok:
    return "We had an error loading your data" 
data = response.json()

def get_pokemon_info(data):
    new_data = []
    for pokemon in data:
        pokemon_dict={}
        pokemon_name = f"{pokemon['forms'][0]['name']}"
        pokemon_dict[pokemon_name]={
            'Name':['forms'][0]['name'],
            'Ability':['abilites'][0]['ability'],
            'Base experience':['abilities']['base_experience'],
            'Sprite URL':['sprites']['front_shiny']
        }
        new_data.append(pokemon_dict)
    return new_data
get_pokemon_info(data)

def get_pokemon_info_by_name(name):
    url = f"https://pokeapi.co/api/v2/{name}"  
    response = requests.get(url)
    if not response.ok:
        return "We had an error loading your data"
    data = response.json()['forms'][0]['name']
    return get_pokemon_info(data)



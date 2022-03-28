import requests
import random

FIRST_GEN_TOTAL = 151
FIRST_GEN_IDS = range(1, FIRST_GEN_TOTAL + 1)

def get_pokemon(pokemon_id):
    return requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}").json()

def get_random_pokemon_list():
    random_pokemon_ids = random.sample(FIRST_GEN_IDS, k=5)
    random_pokemon_list = []
    for pokemon_id in random_pokemon_ids:
        pokemon = get_pokemon(pokemon_id)
        random_pokemon_list.append(pokemon)
    return random_pokemon_list

# def get_random_pokemon_list():
#     random_pokemon_ids = random.sample(FIRST_GEN_IDS, k=5)
#     return [get_pokemon(pokemon_id) for pokemon_id in random_pokemon_ids]

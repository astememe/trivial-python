from os.path import exists
from pprint import pprint

import requests


from requests_net.pokemon import Pokemon
api_url = ""
pokemon_json = {}
nombre = ""

existe = False

def rellenar_tipos(pokemon_json):
    tipos = []
    for tipo in pokemon_json["types"]:
        tipos.append(tipo["type"]["name"])
    return tipos

def rellenar_stats(pokemon_json):
    stats = {}
    for stat in pokemon_json["stats"]:
        stats[stat["stat"]["name"]] = stat['base_stat']
    return stats

def rellenar_descripcion(pokemon_json):
    descripcion = None
    especies = requests.get(pokemon_json['species']['url']).json()
    version = input("De qué versión quieres verlo? (ej. black)\n>>> ")
    for flavor_text in especies["flavor_text_entries"]:
        if flavor_text["version"]["name"] == version:
            descripcion = flavor_text['flavor_text']
    return descripcion

def rellenar_movimientos(pokemon_json):
    movimientos = {}
    for i in range(4):
        movimiento = requests.get(pokemon_json["moves"][i]["move"]["url"]).json()
        nombre = movimiento['name']
        poder = movimiento['power']
        pp = movimiento['pp']
        movimientos[nombre] = {
            "poder": poder,
            "pp": pp
        }
    return movimientos



while not existe:
    try:
        nombre = input("Pokemon a buscar: ")
        api_url = "https://pokeapi.co/api/v2/pokemon/" + nombre
        pokemon_json = requests.get(api_url).json()
        existe = True
    except:
        print("Nombre de pokemon inexistente. Intente de nuevo: ")

pokemon = Pokemon(nombre, rellenar_descripcion(pokemon_json), rellenar_movimientos(pokemon_json), rellenar_tipos(pokemon_json), rellenar_stats(pokemon_json))

print(pokemon)





import utility as util
from data.set_model import PokemonSet


def get_sets():
    list_of_sets = []
    json_list_of_sets = util.file_to_json_obj('data/set_abbreviations.json')
    for json_object in json_list_of_sets:
        list_of_sets.append(PokemonSet.json_to_pokemon_set(json_object))
    return list_of_sets

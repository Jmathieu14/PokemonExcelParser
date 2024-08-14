from typing import List
from constants.pokemon_set_list_constants import get_pokemon_set_abbreviations_file_path
from retrieval.models.pokemon_set_info_response import PokemonSetInfoResponse
import utility as util
from data.models.pokemon_set_model import PokemonSet


def get_sets():
    list_of_sets = []
    json_list_of_sets = util.file_to_json_obj(get_pokemon_set_abbreviations_file_path())
    for json_object in json_list_of_sets:
        list_of_sets.append(PokemonSet.json_to_pokemon_set(json_object))
    return list_of_sets


def find_set_in_sets(set_abbreviation, list_of_sets):
    for pokemon_set in list_of_sets:
        if isinstance(pokemon_set, PokemonSet) and pokemon_set.abbreviation == set_abbreviation:
            return pokemon_set
    return None


def find_set_from_set_code(set_code: str, list_of_sets: List[PokemonSet]):
    for pokemon_set in list_of_sets:
        if pokemon_set.set_code == set_code:
            return pokemon_set
    return None

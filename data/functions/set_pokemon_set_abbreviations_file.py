from typing import List
from constants.pokemon_set_list_constants import get_pokemon_set_abbreviations_file_path
from data.functions.pokemon_set_list_functions import find_set_from_set_code, find_set_in_sets, get_sets
from retrieval.models.pokemon_set_info_response import PokemonSetInfoResponse
import utility as util
import simplejson as j


def add_set_info_to_abbreviations_file(pokemon_set_info_response: PokemonSetInfoResponse):
    json_list_of_sets = util.file_to_json_obj(
        get_pokemon_set_abbreviations_file_path())
    if find_set_in_sets(pokemon_set_info_response.ptcgoCode, get_sets()):
        print('Set %s already in pokemon_set_abbreviations.json' %
              pokemon_set_info_response.ptcgoCode)
    else:
        print('Adding %s to pokemon_set_abbreviations.json' %
              pokemon_set_info_response.ptcgoCode)
        json_list_of_sets.append(j.loads(pokemon_set_info_response.__str__()))
        util.json_object_to_file(json_list_of_sets, get_pokemon_set_abbreviations_file_path())
        

def add_sets_to_abbreviations_file(pokemon_set_info_response_list: List[PokemonSetInfoResponse]):
    json_list_of_sets = util.file_to_json_obj(
        get_pokemon_set_abbreviations_file_path())
    update_required = False
    for pokemon_set_info_response in pokemon_set_info_response_list:
        if not find_set_from_set_code(pokemon_set_info_response.id, get_sets()):
            print('Adding %s, %s to pokemon_set_abbreviations.json' %
                (pokemon_set_info_response.ptcgoCode, pokemon_set_info_response.id))
            json_list_of_sets.append(j.loads(pokemon_set_info_response.__str__()))
            update_required = True
    if update_required:
        util.json_object_to_file(json_list_of_sets, get_pokemon_set_abbreviations_file_path())
    else:
        print('pokemon_set_abbreviations.json is already up to date.')

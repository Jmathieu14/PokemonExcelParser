# Author: Jacques
# Date: 06/07/2020
# Time: 10:45 PM
from data.models.pokemon_set_model import PokemonSet
import utility as util


def get_pokemon_test_set():
    return PokemonSet.json_to_pokemon_set(util.file_to_json_obj('tests/data/test_set_abbreviations.json')[0])

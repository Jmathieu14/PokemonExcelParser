# Author: Jacques
# Date: 11/21/2021
# Time: 3:33 PM
from data.functions.pokemon_deck_functions import decklist_file_to_decklist
from data.functions.pokemon_set_list_functions import get_sets, find_set_in_sets
from data.models.pokemon_deck_summary_model import PokemonDeckSummary


def is_pokemon_deck_buildable(filepath: str):
    deck_to_build = decklist_file_to_decklist(filepath)
    my_sets = get_sets()
    for deck_item in deck_to_build:
        if type(deck_item) != PokemonDeckSummary:
            print('Non-summary item: {0}-{1}-{2}'.format(deck_item.item.get_name(), deck_item.item.get_index(), deck_item.item.get_set().abbreviation))
            find_set_in_sets(deck_item.item.get_set().abbreviation, my_sets)

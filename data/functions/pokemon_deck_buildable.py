# Author: Jacques
# Date: 11/21/2021
# Time: 3:33 PM
from data.functions.pokemon_deck_functions import decklist_file_to_decklist
from data.functions.pokemon_set_list_functions import get_sets, find_set_in_sets
from data.models.pokemon_deck_summary_model import PokemonDeckSummary
from data.models.pokemon_set_model import PokemonSet
from data.models.pokemon_excel_sheet_model import PokemonSetSheet

local_data_set = {}


def is_pokemon_deck_buildable(file_path: str, excel_file_path: str):
    deck_to_build = decklist_file_to_decklist(file_path)
    my_sets = get_sets()
    for deck_item in deck_to_build:
        if type(deck_item) != PokemonDeckSummary:
            item = deck_item.item
            print(
                'Non-summary item: {0}-{1}-{2}'.format(item.get_name(), item.get_index(), item.get_set().abbreviation))
            found_set = find_set_in_sets(item.get_set().abbreviation, my_sets)
            if type(found_set) == PokemonSet and found_set.abbreviation not in local_data_set.keys():
                print('valid set given')
                local_data_set[found_set.abbreviation] = PokemonSetSheet.create(found_set, excel_file_path)
            matching_cards = local_data_set[found_set.abbreviation].get_cards_with_name(item.get_name())
            print(matching_cards)


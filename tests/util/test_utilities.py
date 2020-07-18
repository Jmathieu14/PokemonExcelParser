# Author: Jacques
# Date: 06/07/2020
# Time: 10:45 PM
from pokemontcgsdk import Card

from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from data.models.pokemon_set_model import PokemonSet
import utility as util
from retrieval.models.index_card_model import IndexCard


def get_pokemon_test_set():
    return PokemonSet.json_to_pokemon_set(util.file_to_json_obj('tests/data/test_set_abbreviations.json')[0])


def excel_copy_path(path: str):
    return path.split('.')[0] + '_copy.xlsx'


def empty_index_card():
    return IndexCard(0, Card({}))


def index_card(index: int, name: str, rarity: str):
    card = Card()
    card.name = name
    card.rarity = rarity
    return IndexCard(index, card)


def assert_values_match_those_in_column(values: [], column_index: int, poke_sheet: PokemonSetSheet):
    values_length = values.__len__()
    for i in range(2, values_length + 2):
        poke_sheet_value = poke_sheet.excel_sheet.cell(row=i, column=column_index).value
        if not poke_sheet_value == values[i - 2]:
            print("\nThe value '{0}' at row {1}, column {2} does not match the expected cell value of '{3}'".format(
                    poke_sheet_value,
                    i, column_index,
                    values[i - 2]))
        assert poke_sheet_value == values[i - 2]

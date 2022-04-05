# Author: Jacques
# Date: 06/17/2020
# Time: 8:10 AM
import string

from data.conditional_formatting_config import add_all_formatting_rules_to_sheet
from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from retrieval.models.index_card_model import IndexCard
from retrieval.models.index_cards_model import IndexCards
from retrieval.pokemon_tcg_api import get_cards_from_database, get_cards_not_in_list


def _insert_or_update_sheet_with_index_cards(pokemon_set_sheet: PokemonSetSheet, index_cards: IndexCards,
                                             update_only=True):
    for i in range(0, index_cards.cards.__len__()):
        index_card: IndexCard = index_cards.cards[i]
        card_index = index_card.index
        if not update_only:
            pokemon_set_sheet.insert_card_number(card_index)
        pokemon_set_sheet.update_card_name_with_card_number(index_card.get_name(), card_index)
        pokemon_set_sheet.update_rarity_with_card_number(index_card.get_rarity(), card_index)
        pokemon_set_sheet.update_cell_with_card_number_and_column_name(index_card.get_first_type(), card_index, 'Type')
        print('Added build_card to set sheet: ' + index_card.__str__())


def update_missing_pokemon_metadata(pokemon_set_sheet: PokemonSetSheet):
    card_numbers = pokemon_set_sheet.get_card_numbers_with_missing_data()
    index_cards = get_cards_from_database(pokemon_set_sheet.pokemon_set, card_numbers)
    _insert_or_update_sheet_with_index_cards(pokemon_set_sheet, index_cards)


def insert_complete_set_metadata(pokemon_set_sheet: PokemonSetSheet):
    card_numbers = pokemon_set_sheet.get_card_numbers_in_sheet()
    index_cards = get_cards_not_in_list(pokemon_set_sheet.pokemon_set, card_numbers)
    _insert_or_update_sheet_with_index_cards(pokemon_set_sheet, index_cards, False)


def add_conditional_formatting_from_config(pokemon_set_sheet: PokemonSetSheet):
    add_all_formatting_rules_to_sheet(pokemon_set_sheet.excel_sheet)

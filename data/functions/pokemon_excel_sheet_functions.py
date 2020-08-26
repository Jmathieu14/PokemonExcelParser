# Author: Jacques
# Date: 06/17/2020
# Time: 8:10 AM

from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from retrieval.models.index_card_model import IndexCard
from retrieval.pokemon_tcg_api import get_cards_from_database


def update_missing_pokemon_metadata(pokemon_set_sheet: PokemonSetSheet):
    card_numbers = pokemon_set_sheet.get_card_numbers_with_missing_data()
    index_cards = get_cards_from_database(pokemon_set_sheet.pokemon_set, card_numbers)
    for i in range(0, card_numbers.__len__()):
        index_card: IndexCard = index_cards.cards[i]
        card_index = index_card.index
        name = index_card.get_name()
        rarity = index_card.get_rarity()
        _type = index_card.get_first_type()
        pokemon_set_sheet.update_card_name_with_card_number(name, card_index)
        pokemon_set_sheet.update_rarity_with_card_number(rarity, card_index)
        pokemon_set_sheet.update_cell_with_card_number_and_column_name(_type, card_index, 'Type')

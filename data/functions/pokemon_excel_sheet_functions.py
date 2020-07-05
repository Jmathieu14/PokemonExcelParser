# Author: Jacques
# Date: 06/17/2020
# Time: 8:10 AM

from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from retrieval.pokemon_tcg_api import get_cards_from_database


def update_missing_pokemon_metadata(pokemon_set_sheet: PokemonSetSheet):
    numbers = [1, 2, 3, 4]
    index_cards = get_cards_from_database(pokemon_set_sheet.pokemon_set, numbers)

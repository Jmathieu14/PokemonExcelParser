# Author: Jacques
# Date: 05/30/2020
# Time: 6:06 PM
import time

from pokemontcgsdk import Card, Set
from data.models.pokemon_set_model import PokemonSet
from retrieval.models.index_card_model import IndexCard
from retrieval.models.index_cards_model import IndexCards
from retrieval.models.pokemon_set_info_response import PokemonSetInfoResponse


MAX_REQUESTS_PER_MINUTE = 30
CURRENT_REQUESTS_IN_MINUTE = 0


def get_card_from_database(pokemon_set: PokemonSet, number: int) -> IndexCard:
    search_str = "{0}-{1}".format(pokemon_set.set_code, str(number))
    print("Calling Pokemon TCG API with following search:")
    print(search_str)
    return IndexCard(number, Card.find(search_str))


def get_cards_from_database(pokemon_set: PokemonSet, numbers: [int]) -> IndexCards:
    global CURRENT_REQUESTS_IN_MINUTE
    global MAX_REQUESTS_PER_MINUTE
    index_cards = IndexCards()
    for index in range(0, numbers.__len__()):
        if not CURRENT_REQUESTS_IN_MINUTE < MAX_REQUESTS_PER_MINUTE:
            time.sleep(60)
            CURRENT_REQUESTS_IN_MINUTE = 0
        index_cards.add_index_card(get_card_from_database(pokemon_set, numbers[index]))
        CURRENT_REQUESTS_IN_MINUTE = CURRENT_REQUESTS_IN_MINUTE + 1
    return index_cards


def get_cards_not_in_list(pokemon_set: PokemonSet, numbers: [int]) -> IndexCards:
    last_card_number = get_set_card_count(pokemon_set)
    card_numbers_not_in_list = []
    for x in range(1, last_card_number + 1):
        if x not in numbers:
            card_numbers_not_in_list.append(x)
    return get_cards_from_database(pokemon_set, card_numbers_not_in_list)


def get_set_info(pokemon_set: PokemonSet) -> PokemonSetInfoResponse:
    print('Retrieving ptcgSet information for ptcgSet: ' + pokemon_set.to_str())
    found_set: Set = Set.find(pokemon_set.set_code)
    info = PokemonSetInfoResponse(found_set)
    return info


def get_set_card_count(pokemon_set: PokemonSet) -> int:
    info = get_set_info(pokemon_set)
    return int(info.total)

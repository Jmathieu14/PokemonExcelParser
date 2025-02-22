# Author: Jacques
# Date: 05/30/2020
# Time: 6:06 PM
import time
from typing import List

from pokemontcgsdk import Card, Set
from data.models.pokemon_set_model import PokemonSet
from retrieval.models.index_card_model import IndexCard
from retrieval.models.index_cards_model import IndexCards
from retrieval.models.pokemon_set_info_response import PokemonSetInfoResponse


MAX_REQUESTS_PER_MINUTE = 100
CURRENT_REQUESTS_IN_MINUTE = 0


def handle_request_limit_check():
    global CURRENT_REQUESTS_IN_MINUTE
    global MAX_REQUESTS_PER_MINUTE
    if not CURRENT_REQUESTS_IN_MINUTE < MAX_REQUESTS_PER_MINUTE:
        time.sleep(60)
        CURRENT_REQUESTS_IN_MINUTE = 0
    CURRENT_REQUESTS_IN_MINUTE = CURRENT_REQUESTS_IN_MINUTE + 1


def get_card_from_database(pokemon_set: PokemonSet, number_or_id: int or str) -> IndexCard:
    search_str = "{0}-{1}".format(pokemon_set.set_code, str(number_or_id))
    # Temp Fix for SWSH Promo card search
    if pokemon_set.set_code == 'swshp':
        num_as_str = str(number_or_id)
        while num_as_str.__len__() < 3:
            num_as_str = "0" + num_as_str
        search_str = "{0}-SWSH{1}".format(pokemon_set.set_code, num_as_str)
    handle_request_limit_check()
    print("Calling Pokemon TCG API with following search:")
    print(search_str)
    return IndexCard(number_or_id, Card.find(search_str))


def get_cards_from_database(pokemon_set: PokemonSet, numbers: List[int or str], search_above_total: bool = True) -> IndexCards:
    index_cards = IndexCards()
    set_card_count = get_set_card_count(pokemon_set)
    for index in range(0, numbers.__len__()):
        if (type(numbers[index]) == int and numbers[index] <= set_card_count) or search_above_total:
            index_cards.add_index_card(get_card_from_database(pokemon_set, numbers[index]))
    return index_cards


def get_cards_not_in_list(pokemon_set: PokemonSet, numbers: List[int]) -> IndexCards:
    last_card_number = get_set_card_count(pokemon_set)
    card_numbers_not_in_list = []
    for x in range(1, last_card_number + 1):
        if x not in numbers:
            card_numbers_not_in_list.append(x)
    return get_cards_from_database(pokemon_set, card_numbers_not_in_list)


def get_set_info(pokemon_set: PokemonSet) -> PokemonSetInfoResponse:
    handle_request_limit_check()
    found_set: Set = Set.find(pokemon_set.set_code)
    info = PokemonSetInfoResponse(found_set)
    return info


def get_latest_standard_sets() -> List[PokemonSetInfoResponse]:
    latest_sets: List[Set] = Set.where(q='legalities.standard:legal')
    parsed_latest_sets: List[PokemonSetInfoResponse] = []
    for set in latest_sets:
        parsed_latest_sets.append(PokemonSetInfoResponse(set))
    return parsed_latest_sets


def get_set_card_count(pokemon_set: PokemonSet) -> int:
    info = get_set_info(pokemon_set)
    return int(info.total)

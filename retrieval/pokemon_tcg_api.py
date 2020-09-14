# Author: Jacques
# Date: 05/30/2020
# Time: 6:06 PM
from pokemontcgsdk import Card, Set
from data.models.pokemon_set_model import PokemonSet
from retrieval.models.index_card_model import IndexCard
from retrieval.models.index_cards_model import IndexCards
from retrieval.models.pokemon_set_info_response import PokemonSetInfoResponse


def get_card_from_database(pokemon_set: PokemonSet, number: int) -> IndexCard:
    search_str = "{0}-{1}".format(pokemon_set.set_code, str(number))
    print("Calling Pokemon TCG API with following search:")
    print(search_str)
    return IndexCard(number, Card.find(search_str))


def get_cards_from_database(pokemon_set: PokemonSet, numbers: [int]) -> IndexCards:
    index_cards = IndexCards()
    for index in range(0, numbers.__len__()):
        index_cards.add_index_card(get_card_from_database(pokemon_set, numbers[index]))
    return index_cards


def get_cards_not_in_list(pokemon_set: PokemonSet, numbers: [int]) -> IndexCards:
    pass


def get_set_info(pokemon_set: PokemonSet) -> PokemonSetInfoResponse:
    print('Retrieving ptcgSet information for ptcgSet: ' + pokemon_set.to_str())
    found_set: Set = Set.find(pokemon_set.set_code)
    info = PokemonSetInfoResponse(found_set)
    return info


def get_set_card_count(pokemon_set: PokemonSet) -> int:
    info = get_set_info(pokemon_set)
    return int(info.total_cards)

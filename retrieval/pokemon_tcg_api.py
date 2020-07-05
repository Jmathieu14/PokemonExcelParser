# Author: Jacques
# Date: 05/30/2020
# Time: 6:06 PM
from pokemontcgsdk import Card
from data.models.pokemon_set_model import PokemonSet
from retrieval.models.index_card_model import IndexCard
from retrieval.models.index_cards_model import IndexCards


def get_card_from_database(pokemon_set: PokemonSet, number: int) -> IndexCard:
    return IndexCard(number, Card.find("{0}-{1}".format(pokemon_set.set_code, str(number))))


def get_cards_from_database(pokemon_set: PokemonSet, numbers: [int]) -> IndexCards:
    index_cards = IndexCards()
    for number in range(0, numbers.__len__()):
        index_cards.add_index_card(get_card_from_database(pokemon_set, number))
    return index_cards

# Author: Jacques
# Date: 05/30/2020
# Time: 6:06 PM
from pokemontcgsdk import Card

from data.models.pokemon_set_model import PokemonSet


def get_card_from_database(pokemon_set: PokemonSet, number: int) -> Card:
    return Card.find("{0}-{1}".format(pokemon_set.set_code, str(number)))

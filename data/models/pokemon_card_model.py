# Author: Jacques
# Date: 11/06/2021
# Time: 7:13 PM

# Simpler implementation of type Card from pokemontcgsdk
import re
from typing import Optional, List

from data.models.pokemon_set_model import PokemonSet


class SimplerCard:
    name: str
    rarity: Optional[str]
    types: Optional[List[str]]
    index: Optional[str]

    def __init__(self, name, rarity, types):
        self.name = name
        self.rarity = rarity
        self.types = types

    @staticmethod
    def init_empty():
        return SimplerCard('', '', [])


class PokemonCard:
    def __init__(self, index: int, card: SimplerCard, poke_set: PokemonSet = None):
        self.index = index
        self.card = card
        self._set = poke_set

    @staticmethod
    def builder():
        return PokemonCard(-1, SimplerCard.init_empty())

    def build_index(self, i):
        if type(i) is int:
            self.index = i
            self.card.index = str(i)
        if type(i) is str:
            if re.search('[A-z]', i) is None:
                self.index = int(i)
            self.card.index = i
        return self

    def name(self, name: str):
        self.card.name = name
        return self

    def build_set(self, poke_set: PokemonSet):
        self._set = poke_set
        return self

    def get_name(self):
        return self.card.name

    def get_index(self):
        return self.index

    def get_set(self):
        return self._set

    def get_rarity(self):
        return self.card.rarity

    def get_first_type(self):
        first_type = 'N/A'
        if self.card.types is not None and self.card.types.__len__() > 0:
            first_type = self.card.types[0]
        return first_type

    def __eq__(self, other):
        if not (type(other) == PokemonCard):
            return False
        return self.get_name() == other.get_name() and \
               self.get_rarity() == other.get_rarity() and \
               self.get_first_type() == other.get_first_type() and \
               self.get_index() == other.get_index() and \
               self.get_set() == other.get_set()

    def __str__(self):
        return "PokemonCard: [ index: {0}, name: {1}, rarity: {2}, type: {3} ]".format(
            self.index,
            self.get_name(),
            self.get_rarity(),
            self.get_first_type())


class PokemonCardInfo:
    card: PokemonCard
    count: int

    def __init__(self, card, count):
        self.card = card
        self.count = count

    @staticmethod
    def builder():
        default_card = PokemonCard.builder()
        return PokemonCardInfo(default_card, 0)

    def build_card(self, card: PokemonCard):
        self.card = card
        return self

    def build_count(self, count: int):
        self.count = count
        return self

    def get_card(self):
        return self.card

    def get_count(self):
        return self.count

    def __eq__(self, other):
        if type(other) is not PokemonCardInfo:
            return False
        return self.count == other.count and \
               self.card.__eq__(other.build_card)

    def __str__(self):
        return "PokemonCardInfo: [\n\tcount: {0},\n\tcard: {1}\n]".format(self.count, self.card.__str__())

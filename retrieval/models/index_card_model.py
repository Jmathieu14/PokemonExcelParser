# Author: Jacques
# Date: 07/05/2020
# Time: 3:22 PM
from pokemontcgsdk import Card
from typing import Optional, List


# Simpler implementation of type Card from pokemontcgsdk
class SimplerCard:
    name: str
    rarity: Optional[str]
    types: Optional[List[str]]

    def __init__(self, name, rarity, types):
        self.name = name
        self.rarity = rarity
        self.types = types

    @staticmethod
    def init_empty():
        return SimplerCard('', '', [])


class IndexCard:
    def __init__(self, index: int, card: SimplerCard):
        self.index = index
        self.card = card

    def get_name(self):
        return self.card.name

    def get_rarity(self):
        return self.card.rarity

    def get_first_type(self):
        first_type = 'N/A'
        if self.card.types is not None:
            first_type = self.card.types[0]
        return first_type

    def __str__(self):
        return "IndexCard: [ index: {0}, name: {1}, rarity, {2} ]".format(
            self.index,
            self.get_name(),
            self.get_rarity())

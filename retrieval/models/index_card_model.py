# Author: Jacques
# Date: 07/05/2020
# Time: 3:22 PM
from pokemontcgsdk import Card


class IndexCard:
    def __init__(self, index: int, card: Card):
        self.index = index
        self.card = card

    def get_name(self):
        return self.card.name

    def get_rarity(self):
        return self.card.rarity

    def get_first_type(self):
        first_type = self.card.types[0]
        return first_type if first_type is not None else 'N/A'

    def __str__(self):
        return "IndexCard: [ index: {0}, name: {1}, rarity, {2} ]".format(
            self.index,
            self.get_name(),
            self.get_rarity())

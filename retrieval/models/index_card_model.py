# Author: Jacques
# Date: 07/05/2020
# Time: 3:22 PM
from pokemontcgsdk import Card


class IndexCard:
    def __init__(self, index: int, card: Card):
        self.index = index
        self.card = card

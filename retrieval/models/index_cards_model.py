# Author: Jacques
# Date: 07/05/2020
# Time: 3:24 PM
from pokemontcgsdk import Card
from retrieval.models.index_card_model import IndexCard


class IndexCards:
    def __init__(self):
        self.cards = []

    def add_index_and_card(self, index: int, card: Card):
        self.cards.append(IndexCard(index, card))

    def add_index_card(self, index_card: IndexCard):
        self.cards.append(index_card)

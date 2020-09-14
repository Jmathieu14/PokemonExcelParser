# Author: Jacques
# Date: 09/14/2020
# Time: 3:24 PM
from pokemontcgsdk import Set


class PokemonSetInfoResponse:
    def __init__(self, ptcg_set: Set):
        self.code = ptcg_set.code
        self.total_cards = ptcg_set.total_cards
        self.name = ptcg_set.name
        self.ptcgo_code = ptcg_set.ptcgo_code
        self.release_date = ptcg_set.release_date

    def __str__(self):
        return "['code': {0}, 'total_cards': {1}, 'name': {2}, 'ptcgo_code': {3}]"\
                .format(self.code, self.total_cards, self.name, self.ptcgo_code)

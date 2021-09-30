# Author: Jacques
# Date: 09/14/2020
# Time: 3:24 PM
from pokemontcgsdk import Set


class PokemonSetInfoResponse:
    def __init__(self, ptcg_set: Set):
        self.code = ptcg_set.id
        self.total_cards = ptcg_set.total
        self.name = ptcg_set.name
        self.ptcgo_code = ptcg_set.ptcgoCode
        self.release_date = ptcg_set.releaseDate
        self.series = ptcg_set.series

    def __str__(self):
        return "{{\"set_code\": \"{0}\"," \
               " \"total_cards\": \"{1}\"," \
               " \"name\": \"{2}\"," \
               " \"abbreviation\": \"{3}\"," \
               " \"series\": \"{4}\"}}"\
                .format(self.code, self.total_cards, self.name, self.ptcgo_code, self.series)

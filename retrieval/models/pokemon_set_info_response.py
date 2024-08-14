# Author: Jacques
# Date: 09/14/2020
# Time: 3:24 PM
from pokemontcgsdk import Set
from typing import Optional


class PokemonSetInfoResponse:
    id: str
    total: int
    name: str
    ptcgoCode: Optional[str]
    releaseDate: str
    series: str
    standard_legal: bool

    def __init__(self, ptcg_set: Set):
        self.id = ptcg_set.id
        self.total = ptcg_set.total
        self.name = ptcg_set.name
        self.ptcgoCode = ptcg_set.ptcgoCode
        self.releaseDate = ptcg_set.releaseDate
        self.series = ptcg_set.series
        self.standard_legal = False
        if (ptcg_set.legalities.standard == 'Legal'):
            self.standard_legal = True

    def __str__(self):
        return "{{\"set_code\": \"{0}\"," \
               " \"total\": \"{1}\"," \
               " \"name\": \"{2}\"," \
               " \"abbreviation\": \"{3}\"," \
               " \"standard_legal\": \"{4}\"," \
               " \"release_date\": \"{5}\", " \
               " \"series\": \"{6}\"}}"\
                .format(self.id, self.total, self.name, self.ptcgoCode, self.standard_legal, self.releaseDate, self.series)

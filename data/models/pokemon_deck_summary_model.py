# Author: Jacques
# Date: 11/07/2021
# Time: 1:30 PM


class PokemonDeckSummary:
    def __init__(self, summary_type: str, total: int):
        self.summary_type = summary_type
        self.total = total

    def __eq__(self, other):
        if not (type(other) == PokemonDeckSummary):
            return False
        return self.summary_type == other.summary_type and \
               self.total == other.total

    def __str__(self):
        return "PokemonDeckSummary: [ summary_type: {0}, total: {1} ]".format(self.summary_type, self.total)

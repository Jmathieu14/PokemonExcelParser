# Author: Jacques
# Date: 11/07/2021
# Time: 2:17 PM


class PokemonDeckItem:
    def __init__(self, item, count: int):
        self.item = item
        self.count = count

    def __eq__(self, other):
        if not(type(other) == PokemonDeckItem):
            return False
        return self.item == other.item and \
               self.count == other.count

    def __str__(self):
        return "PokemonDeckItem: [ item: {0}, count: {1} ]".format(self.item, self.count)

# Author: Jacques
# Date: 07/03/2020
# Time: 9:41 PM


class PokeColumn:
    def __init__(self, name: str, preferred_index: int):
        self.name = '' if name is None else name
        self.index = preferred_index

    def column_name_matches(self, other_poke_column):
        return self.name.lower() == other_poke_column.name.lower()

    def equals(self, other_poke_column):
        return self.column_name_matches(other_poke_column) and self.index == other_poke_column.index

    def __str__(self):
        return "PokeColumn: ['name': '{0}', 'index': '{1}']".format(
            self.name,
            self.index)

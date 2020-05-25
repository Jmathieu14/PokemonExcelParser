

class PokemonSet:
    def __init__(self, abbreviation, name, series):
        self.abbreviation = abbreviation
        self.name = name
        self.series = series

    def json_to_pokemon_set(json_object):
        return PokemonSet(json_object['abbreviation'], json_object['name'], json_object['series'])

    def to_str(self):
        return "['abbr': '{0}', 'name': '{1}', 'series': '{2}']".format(self.abbreviation, self.name, self.series)

    def print(self):
        print(self.to_str())

    def print_list(set_list):
        for set in set_list:
            if isinstance(set, PokemonSet):
                set.print()
                print("\n")

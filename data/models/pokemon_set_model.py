class PokemonSet:
    def __init__(self, abbreviation, name, series, set_code):
        self.abbreviation = abbreviation
        self.name = name
        self.series = series
        self.set_code = set_code

    def json_to_pokemon_set(json_object):
        return PokemonSet(json_object['abbreviation'], json_object['name'], json_object['series'],
                          json_object['set_code'])

    def to_str(self):
        return "['abbr': '{0}', 'name': '{1}', 'series': '{2}', 'set_code': '{3}']".format(
            self.abbreviation,
            self.name,
            self.series,
            self.set_code)

    def print(self):
        print(self.to_str())

    def print_list(set_list):
        for set in set_list:
            if isinstance(set, PokemonSet):
                set.print()
                print("\n")


def create_dummy_set_from_set_code(set_code: str):
    return PokemonSet('DUMMY', 'DUMMY', 'DUMMY', set_code)

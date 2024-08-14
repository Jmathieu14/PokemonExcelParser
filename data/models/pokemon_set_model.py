from data.utility import str2bool


class PokemonSet:
    def __init__(self, abbreviation, name, series, set_code, standard_legal):
        self.abbreviation = abbreviation
        self.name = name
        self.series = series
        self.set_code = set_code
        self.standard_legal = standard_legal

    def json_to_pokemon_set(json_object):
        standard_legal = False
        if 'standard_legal' in json_object:
            standard_legal = str2bool(json_object['standard_legal'])
        return PokemonSet(json_object['abbreviation'], json_object['name'], json_object['series'],
                          json_object['set_code'], standard_legal)

    def to_str(self):
        return "['abbr': '{0}', 'name': '{1}', 'series': '{2}', 'set_code': '{3}', 'standard_legal': '{4}']".format(
            self.abbreviation,
            self.name,
            self.series,
            self.set_code,
            self.standard_legal)

    def print(self):
        print(self.to_str())

    def print_list(set_list):
        for set in set_list:
            if isinstance(set, PokemonSet):
                set.print()
                print("\n")

    def __eq__(self, other):
        if not(type(other) == PokemonSet):
            return False
        return self.name == other.name and \
               self.abbreviation == other.abbreviation and \
               self.series == other.series and \
               self.set_code == other.set_code and \
               self.standard_legal == other.standard_legal


def create_dummy_set_from_set_code(set_code: str):
    return PokemonSet('DUMMY', 'DUMMY', 'DUMMY', set_code, True)

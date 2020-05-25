import data.functions.pokemon_set_list_functions
from data.models.pokemon_set_model import PokemonSet


def main():
    my_sets = data.functions.pokemon_set_list_functions.get_sets()
    PokemonSet.print_list(my_sets)


if __name__ == '__main__':
    main()

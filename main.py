import data.get_sets
from data.set_model import PokemonSet


def main():
    my_sets = data.get_sets.get_sets()
    PokemonSet.print_list(my_sets)


if __name__ == '__main__':
    main()

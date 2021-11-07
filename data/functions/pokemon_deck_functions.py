# Author: Jacques
# Date: 11/06/2021
# Time: 8:08 PM
from data.functions.pokemon_set_list_functions import get_sets, find_set_in_sets
from data.models.pokemon_card_model import PokemonCard

MY_SETS = get_sets()


def deck_line_to_cards(line: str):
    words = line.split(" ")
    count = int(words[0])
    index = int(words[-1])
    word_count = words.__len__()
    set_code = words[word_count - 2]
    poke_set = find_set_in_sets(set_code, MY_SETS)
    name = " ".join(words[1:word_count-2]).strip()
    cards = [count]
    for i in range(0, count):
        cards[i] = PokemonCard.builder().name(name).build_index(index).build_set(poke_set)
    return cards

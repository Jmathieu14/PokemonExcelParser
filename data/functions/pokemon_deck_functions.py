# Author: Jacques
# Date: 11/06/2021
# Time: 8:08 PM
from typing import List
from data.functions.pokemon_set_list_functions import get_sets, find_set_in_sets
from data.models.pokemon_card_model import PokemonCard
from data.models.pokemon_deck_item_model import PokemonDeckItem
from data.models.pokemon_deck_summary_model import PokemonDeckSummary
from utility import file_exists

MY_SETS = get_sets()


# https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python
def has_int_value(s: str):
    try:
        int(s)
        return True
    except ValueError:
        return False


def parse_line_as_cards_item(words: List[str]):
    count = int(words[0])
    index = int(words[-1])
    word_count = words.__len__()
    set_code = words[word_count - 2]
    poke_set = find_set_in_sets(set_code, MY_SETS)
    name = " ".join(words[1:word_count - 2]).strip()
    card = PokemonCard.builder().name(name).build_index(index).build_set(poke_set)
    cards_item = PokemonDeckItem(item=card, count=count)
    return cards_item


def parse_line_as_summary(words: List[str]):
    return PokemonDeckSummary(summary_type=words[0], total=int(words[2]))


def deck_line_to_item(line: str):
    words = line.split(" ")
    if has_int_value(words[0]):
        return parse_line_as_cards_item(words)
    else:
        return parse_line_as_summary(words)


def deck_lines_to_deck_list(lines: List[str]):
    deck_list = []
    for line in lines:
        item = deck_line_to_item(line)
        deck_list.append(item)
    return deck_list


def deck_list_file_to_deck_list(filepath: str):
    if file_exists(filepath):
        with open(filepath, 'r') as my_deck:
            deck_lines = my_deck.readlines()
            my_deck.close()
        return deck_lines_to_deck_list(deck_lines)

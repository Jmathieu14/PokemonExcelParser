# Author: Jacques
# Date: 11/06/2021
# Time: 7:52 PM

import unittest
from data.functions.pokemon_deck_functions import deck_line_to_item, deck_lines_to_deck_list, \
    decklist_file_to_decklist
from data.models.pokemon_card_model import PokemonCard
from data.models.pokemon_deck_item_model import PokemonDeckItem
from data.models.pokemon_deck_summary_model import PokemonDeckSummary
from data.models.pokemon_set_model import PokemonSet

deck_line_one = "1 Air Balloon SSH 156"
swsh1 = PokemonSet("SSH", "Sword & Shield", "Sword & Shield", "swsh1", False)
deck_line_multiple_cards = "2 Zacian V CEL 16"
cel25 = PokemonSet("CEL", "Celebrations", "Sword & Shield", "cel25", False)
air_balloon = PokemonCard.builder() \
    .name("Air Balloon") \
    .build_index(156) \
    .build_set(swsh1)
air_balloon_deck_item = PokemonDeckItem(item=air_balloon, count=1)
zacian_v = PokemonCard.builder() \
    .name("Zacian V") \
    .build_index(16) \
    .build_set(cel25)
zacian_v_deck_item = PokemonDeckItem(item=zacian_v, count=2)
deck_line_pokemon_summary_text = "Pokemon - 3"
pokemon_summary = PokemonDeckSummary(summary_type="Pokemon", total=3)
pokemon_summary_2 = PokemonDeckSummary(summary_type="Pokemon", total=2)
trainer_summary = PokemonDeckSummary(summary_type="Trainer", total=1)


class TestPokemonDeck(unittest.TestCase):
    def test_deck_line_to_item__makes_expected_item_with_count_1(self):
        actual_item = deck_line_to_item(deck_line_one)
        assert actual_item == air_balloon_deck_item

    def test_deck_line_to_item__makes_expected_item_with_count_2(self):
        actual_item = deck_line_to_item(deck_line_multiple_cards)
        assert actual_item == zacian_v_deck_item

    def test_deck_line_to_item__makes_expected_summary_item(self):
        actual_item = deck_line_to_item(deck_line_pokemon_summary_text)
        assert actual_item == pokemon_summary

    def test_deck_lines_to_deck_list__makes_expected_deck_list(self):
        actual_deck_list = deck_lines_to_deck_list([deck_line_one, deck_line_multiple_cards])
        assert actual_deck_list.__len__() == 2
        assert actual_deck_list[0] == air_balloon_deck_item
        assert actual_deck_list[1] == zacian_v_deck_item

    def test_deck_lines_to_deck_list__makes_expected_deck_list_with_summary(self):
        actual_deck_list = deck_lines_to_deck_list(
            [deck_line_pokemon_summary_text, deck_line_one, deck_line_multiple_cards])
        assert actual_deck_list.__len__() == 3
        assert actual_deck_list[0] == pokemon_summary
        assert actual_deck_list[1] == air_balloon_deck_item
        assert actual_deck_list[2] == zacian_v_deck_item

    def test_deck_list_file_to_deck_list__makes_expected_deck_list(self):
        actual_deck_list = decklist_file_to_decklist('tests/data/test_simple_deck_list.ptcgo.txt')
        assert actual_deck_list.__len__() == 4
        assert actual_deck_list[0] == pokemon_summary_2
        assert actual_deck_list[1] == zacian_v_deck_item
        assert actual_deck_list[2] == trainer_summary
        assert actual_deck_list[3] == air_balloon_deck_item


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonDeck)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

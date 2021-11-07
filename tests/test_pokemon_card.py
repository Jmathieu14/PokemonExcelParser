# Author: Jacques
# Date: 11/06/2021
# Time: 7:52 PM

import unittest
from data.functions.pokemon_deck_functions import deck_line_to_items, deck_lines_to_deck_list
from data.models.pokemon_card_model import PokemonCard
from data.models.pokemon_deck_summary_model import PokemonDeckSummary
from data.models.pokemon_set_model import PokemonSet

deck_line_one = "1 Air Balloon SSH 156"
swsh1 = PokemonSet("SSH", "Sword & Shield", "Sword & Shield", "swsh1")
deck_line_multiple_cards = "2 Zacian V CEL 16"
cel25 = PokemonSet("CEL", "Celebrations", "Sword & Shield", "cel25")
air_balloon = PokemonCard.builder() \
    .name("Air Balloon") \
    .build_index(156) \
    .build_set(swsh1)
zacian_v = PokemonCard.builder() \
    .name("Zacian V") \
    .build_index(16) \
    .build_set(cel25)
deck_line_pokemon_summary_text = "Pokemon - 3"
pokemon_summary = PokemonDeckSummary(summary_type="Pokemon", total=3)


class TestPokemonCard(unittest.TestCase):
    def test_deck_line_to_items__makes_expected_card(self):
        actual_cards = deck_line_to_items(deck_line_one)
        assert actual_cards[0].__eq__(air_balloon)

    def test_deck_line_to_items__makes_expected_card_list(self):
        actual_cards = deck_line_to_items(deck_line_multiple_cards)
        assert actual_cards.__len__() == 2
        assert actual_cards[0] == zacian_v and actual_cards[1] == zacian_v

    def test_deck_lines_to_items__makes_expected_card_list(self):
        actual_cards = deck_lines_to_deck_list([deck_line_one, deck_line_multiple_cards])
        assert actual_cards.__len__() == 3
        assert actual_cards[0] == air_balloon
        assert actual_cards[1] == zacian_v and actual_cards[2] == zacian_v

    def test_deck_line_to_items__makes_expected_summary_item(self):
        actual_items = deck_line_to_items(deck_line_pokemon_summary_text)
        assert actual_items[0] == pokemon_summary

    def test_deck_lines_to_deck_list__makes_expected_deck_list(self):
        actual_deck_list = deck_lines_to_deck_list(
            [deck_line_pokemon_summary_text, deck_line_one, deck_line_multiple_cards])
        assert actual_deck_list.__len__() == 4
        assert actual_deck_list[0] == pokemon_summary
        assert actual_deck_list[1] == air_balloon
        assert actual_deck_list[2] == zacian_v and actual_deck_list[3] == zacian_v


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonCard)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

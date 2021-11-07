# Author: Jacques
# Date: 11/06/2021
# Time: 7:52 PM

import unittest
from data.functions.pokemon_deck_functions import deck_line_to_cards
from data.models.pokemon_card_model import PokemonCard
from data.models.pokemon_set_model import PokemonSet

deck_line_one = "1 Air Balloon SSH 156"
swsh1 = PokemonSet("SSH", "Sword & Shield", "Sword & Shield", "swsh1")


class TestPokemonCard(unittest.TestCase):
    def test_deck_line_to_cards__makes_expected_card(self):
        expected_card = PokemonCard.builder()\
            .name("Air Balloon")\
            .build_index(156)\
            .build_set(swsh1)
        actual_cards = deck_line_to_cards(deck_line_one)
        assert actual_cards[0].__eq__(expected_card)


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonCard)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

import unittest
import unittest.mock as mock
from pokemontcgsdk import Card

from retrieval.models.index_card_model import IndexCard
from retrieval.models.index_cards_model import IndexCards
from tests.util.test_utilities import get_pokemon_test_set, empty_index_card

test_pokemon_set = get_pokemon_test_set()


class TestPokemonTcgApi(unittest.TestCase):
    @mock.patch('retrieval.pokemon_tcg_api.get_card_from_database')
    def test_get_card_from_database_should_return_card(self, mock_get_card_from_database):
        mock_get_card_from_database.return_value = empty_index_card()
        assert type(mock_get_card_from_database(test_pokemon_set, 1)) is IndexCard

    @mock.patch('retrieval.pokemon_tcg_api.get_cards_from_database')
    def test_get_cards_from_database_should_return_list_of_cards(self, mock_get_cards_from_database):
        index_cards = IndexCards()
        index_cards.cards = [empty_index_card(), empty_index_card(), empty_index_card(), empty_index_card()]
        mock_get_cards_from_database.return_value = index_cards
        card_numbers_for_lookup = [1, 2, 3, 4]
        value_returned = mock_get_cards_from_database(test_pokemon_set, card_numbers_for_lookup)
        assert type(value_returned) is IndexCards
        assert type(value_returned.cards[0]) is IndexCard


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonTcgApi)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

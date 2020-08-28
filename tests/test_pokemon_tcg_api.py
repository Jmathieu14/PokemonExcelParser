import unittest
import unittest.mock as mock

from retrieval.models.index_card_model import IndexCard
from retrieval.models.index_cards_model import IndexCards
from retrieval.pokemon_tcg_api import get_set_card_count, get_set_info
from tests.util.test_utilities import get_pokemon_test_set, empty_index_card, MockSet

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

    @mock.patch('retrieval.pokemon_tcg_api.get_set_info')
    def test_get_set_card_count__should_call_get_set_info(self, mock_get_set_info):
        get_set_card_count(get_pokemon_test_set())
        mock_get_set_info.assert_called()

    @mock.patch('pokemontcgsdk.Set.find')
    def test_get_set_info__should_return_code_count_and_call_set_find(self, mock_set_find):
        expected_info = {'code': 'my_code', 'total_cards': '900'}
        mock_return_value = MockSet(expected_info['code'], expected_info['total_cards'])
        mock_set_find.return_value = mock_return_value
        actual_info = get_set_info(get_pokemon_test_set())
        mock_set_find.assert_called_with(get_pokemon_test_set().set_code)
        assert actual_info == expected_info


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonTcgApi)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

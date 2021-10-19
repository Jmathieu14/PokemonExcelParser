import unittest
import unittest.mock as mock

from retrieval.models.index_card_model import IndexCard
from retrieval.models.index_cards_model import IndexCards
from retrieval.models.pokemon_set_info_response import PokemonSetInfoResponse
from retrieval.pokemon_tcg_api import get_set_card_count, get_set_info, get_cards_not_in_list, get_cards_from_database
from tests.util.test_utilities import get_pokemon_test_set, empty_index_card, makeDummySet

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
    def test_get_set_info__should_call_set_find(self, mock_set_find):
        mock_return_value = PokemonSetInfoResponse(makeDummySet(1))
        print('put mock set in set info response object')
        mock_set_find.return_value = mock_return_value
        get_set_info(get_pokemon_test_set())
        mock_set_find.assert_called_with(get_pokemon_test_set().set_code)

    @mock.patch('retrieval.pokemon_tcg_api.get_cards_from_database')
    def test_get_cards_not_in_list__should_call_get_cards_from_database(self, mock_get_cards_from_database):
        mock_get_set_card_count = mock.patch('retrieval.pokemon_tcg_api.get_set_card_count', return_value=5)
        mock_get_set_card_count.start()
        cards_in_list = [1, 2, 4]
        expected_card_number_list = [3, 5]
        get_cards_not_in_list(test_pokemon_set, cards_in_list)
        mock_get_cards_from_database.assert_called_with(test_pokemon_set, expected_card_number_list)

    @mock.patch('retrieval.pokemon_tcg_api.get_cards_from_database')
    def test_get_cards_not_in_list__should_skip_calls_for_cards_above_set_card_count(self, mock_get_cards_from_database):
        mock_get_set_card_count = mock.patch('retrieval.pokemon_tcg_api.get_set_card_count', return_value=5)
        mock_get_set_card_count.start()
        cards_in_list = [1, 2, 4, 6, 9]
        expected_card_number_list = [3, 5]
        get_cards_not_in_list(test_pokemon_set, cards_in_list)
        mock_get_cards_from_database.assert_called_with(test_pokemon_set, expected_card_number_list)

    @mock.patch('retrieval.pokemon_tcg_api.get_card_from_database')
    def test_get_cards_from_database__should_skip_calls_for_cards_above_set_card_count(self, mock_get_card_from_database):
        mock_get_set_card_count = mock.patch('retrieval.pokemon_tcg_api.get_set_card_count', return_value=5)
        mock_get_set_card_count.start()
        card_numbers = [6, 9]
        get_cards_from_database(test_pokemon_set, card_numbers)
        mock_get_card_from_database.assert_not_called()


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonTcgApi)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

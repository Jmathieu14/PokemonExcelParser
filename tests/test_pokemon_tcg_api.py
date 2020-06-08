import unittest
import unittest.mock as mock
from pokemontcgsdk import Card
from tests.functions.get_pokemon_test_set import get_pokemon_test_set

test_pokemon_set = get_pokemon_test_set()


class TestPokemonTcgApi(unittest.TestCase):
    @mock.patch('retrieval.pokemon_tcg_api.get_card_from_database')
    def test_get_card_from_database_should_return_card(self, mock_get_card_from_database):
        mock_get_card_from_database.return_value = Card({})
        assert type(mock_get_card_from_database(test_pokemon_set, 1)) is Card


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonTcgApi)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

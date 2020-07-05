import os
import shutil
import unittest
from unittest import mock

from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from tests.util.test_utilities import get_pokemon_test_set, excel_copy_path

test_pokemon_set = get_pokemon_test_set()


class TestPokemonSetSheetFunctions(unittest.TestCase):
    @mock.patch('retrieval.pokemon_tcg_api.get_cards_from_database')
    def test_update_missing_pokemon_metadata__calls_tcg_api(self, mock_get_cards_from_database):
        test_path = 'tests/data/test_update_missing_metadata.xlsx'
        shutil.copy2(test_path, excel_copy_path(test_path))
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, excel_copy_path(test_path))
        os.remove(excel_copy_path(test_path))


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonSetSheetFunctions)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

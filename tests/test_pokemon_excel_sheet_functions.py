import os
import shutil
import unittest
from unittest import mock

from data.functions.pokemon_excel_sheet_functions import update_missing_pokemon_metadata
from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from retrieval.models.index_cards_model import IndexCards
from tests.util.test_utilities import get_pokemon_test_set, excel_copy_path, index_card, \
    assert_values_match_those_in_column, assert_not_called_with

mock.Mock.assert_not_called_with = assert_not_called_with

test_pokemon_set = get_pokemon_test_set()


class TestPokemonSetSheetFunctions(unittest.TestCase):
    @mock.patch('data.functions.pokemon_excel_sheet_functions.get_cards_from_database')
    def test_update_missing_pokemon_metadata__calls_tcg_api(self, mock_get_cards_from_database):
        test_path = 'tests/data/test_update_missing_metadata.xlsx'
        shutil.copy2(test_path, excel_copy_path(test_path))
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, excel_copy_path(test_path))
        update_missing_pokemon_metadata(my_set_sheet)
        mock_get_cards_from_database.assert_called_once_with(test_pokemon_set, [1, 2, 3, 4])
        os.remove(excel_copy_path(test_path))

    @mock.patch('data.functions.pokemon_excel_sheet_functions.get_cards_from_database')
    def test_update_missing_pokemon_metadata__should_update_missing_data(self, mock_get_cards_from_database):
        index_cards = IndexCards()
        index_cards.cards = [index_card(1, "Pikachu", "Common", "Electric"),
                             index_card(2, "Raichu", "Uncommon", "Electric"),
                             index_card(3, "Pichu", "Uncommon", "Electric"),
                             index_card(4, "Jigglypuff", "Common", "Normal")]
        mock_get_cards_from_database.return_value = index_cards
        test_path = 'tests/data/test_update_missing_metadata.xlsx'
        shutil.copy2(test_path, excel_copy_path(test_path))
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, excel_copy_path(test_path))
        update_missing_pokemon_metadata(my_set_sheet)
        col_1_expected_values = ["Pikachu", "Raichu", "Pichu", "Jigglypuff"]
        col_4_expected_values = ["Common", "Uncommon", "Uncommon", "Common"]
        col_5_expected_values = ["Electric", "Electric", "Electric", "Normal"]
        assert_values_match_those_in_column(col_1_expected_values, 1, my_set_sheet)
        assert_values_match_those_in_column(col_4_expected_values, 4, my_set_sheet)
        assert_values_match_those_in_column(col_5_expected_values, 5, my_set_sheet)
        os.remove(excel_copy_path(test_path))

    @mock.patch('data.functions.pokemon_excel_sheet_functions.get_cards_from_database')
    def test_update_missing_pokemon_metadata__calls_tcg_api_with_missing_card_numbers\
                    (self, mock_get_cards_from_database):
        test_path = 'tests/data/test_update_missing_metadata_v2.xlsx'
        shutil.copy2(test_path, excel_copy_path(test_path))
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, excel_copy_path(test_path))
        update_missing_pokemon_metadata(my_set_sheet)
        mock_get_cards_from_database.assert_called_once_with(test_pokemon_set, [1, 3, 4])
        os.remove(excel_copy_path(test_path))

    @mock.patch('data.functions.pokemon_excel_sheet_functions.get_cards_from_database')
    def test_update_missing_pokemon_metadata__does_not_call_tcg_api_when_all_required_columns_are_filled\
                    (self, mock_get_cards_from_database):
        test_path = 'tests/data/test_update_missing_metadata__not_called__required_columns_filled.xlsx'
        shutil.copy2(test_path, excel_copy_path(test_path))
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, excel_copy_path(test_path))
        update_missing_pokemon_metadata(my_set_sheet)
        mock_get_cards_from_database.assert_not_called_with(test_pokemon_set, [2])
        os.remove(excel_copy_path(test_path))


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonSetSheetFunctions)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

import unittest
import unittest.mock as mock
import shutil
import os

from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from data.models.pokemon_excel_sheet_model import get_poke_columns_config
from data.models.pokemon_set_model import PokemonSet
from data.models.pokemon_column_model import PokeColumn
from tests.util.test_utilities import get_pokemon_test_set, excel_copy_path, assert_values_match_those_in_column
import data.models.pokemon_excel_sheet_model as pokemon_excel_sheet_model

base_pokemon_sheet_model_import = 'data.models.pokemon_excel_sheet_model'
get_excel_sheet_import = base_pokemon_sheet_model_import + '._get_excel_workbook_from_file'

test_pokemon_set = get_pokemon_test_set()


class TestPokemonSetSheet(unittest.TestCase):

    def setUp(self):
        pokemon_excel_sheet_model.DEBUG_MODE = True

    def test_debug_mode_on(self):
        assert pokemon_excel_sheet_model.DEBUG_MODE

    @mock.patch(get_excel_sheet_import)
    def test_create_should_call_get_excel_workbook_from_file(self, mock_get_excel_workbook_from_file):
        PokemonSetSheet.create(PokemonSet(None, None, None, None, False), None)
        assert mock_get_excel_workbook_from_file.called

    def test_should_have_correct_poke_columns(self):
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, 'tests/data/test_pokemon_excel_sheet.xlsx')
        assert_column_is_in_sheet(PokeColumn('Card #', 1), my_set_sheet)
        assert_column_is_in_sheet(PokeColumn('4 Owned', 2), my_set_sheet)
        assert my_set_sheet.is_poke_column_in_columns(PokeColumn('CardZ #99 bloppp', 40)) is False

    def test_should_have_correct_values(self):
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, 'tests/data/test_pokemon_excel_sheet.xlsx')
        col_1_expected_values = [1, 2, 3, 4]
        col_2_expected_values = ['Yes', 'Yes', 'Yes', 'Yes']
        assert_values_match_those_in_column(col_1_expected_values, 1, my_set_sheet)
        assert_values_match_those_in_column(col_2_expected_values, 2, my_set_sheet)

    def test_move_existing_columns_out_of_way(self):
        test_path = 'tests/data/test_move_existing_columns_away.xlsx'
        shutil.copy2(test_path, excel_copy_path(test_path))
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, excel_copy_path(test_path))
        my_set_sheet.move_existing_columns_out_of_way()
        poke_column_config_size = get_poke_columns_config().__len__()
        expected_columns = [PokeColumn('Card #', 3 + poke_column_config_size),
                            PokeColumn('4 Owned', 4 + poke_column_config_size)]

        for i in range(poke_column_config_size + 3, poke_column_config_size + 3 + expected_columns.__len__()):
            expected_columns_index = i - 3 - poke_column_config_size
            assert my_set_sheet.is_poke_column_in_columns(expected_columns[expected_columns_index])
        os.remove(excel_copy_path(test_path))

    def test_move_existing_columns_to_proper_index(self):
        test_path = 'tests/data/test_pokemon_excel_sheet.xlsx'
        shutil.copy2(test_path, excel_copy_path(test_path))
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, excel_copy_path(test_path))
        my_set_sheet.move_existing_columns_out_of_way()
        my_set_sheet.move_existing_columns_to_proper_index()
        poke_column_config = get_poke_columns_config()
        col_config_length = poke_column_config.__len__()
        for i in range(0, col_config_length):
            if poke_column_config[i].name == "4 Owned" or poke_column_config[i].name == "Card #":
                assert_column_is_in_sheet(poke_column_config[i], my_set_sheet)
        os.remove(excel_copy_path(test_path))

    def test_insert_missing_columns(self):
        test_path = 'tests/data/test_insert_missing_columns.xlsx'
        shutil.copy2(test_path, excel_copy_path(test_path))
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, excel_copy_path(test_path))
        col_2_expected_values = [1, 2, 3, 4]
        col_3_expected_values = ['Yes', 'Yes', 'Yes', 'Yes']
        assert_values_match_those_in_column(col_2_expected_values, 2, my_set_sheet)
        assert_values_match_those_in_column(col_3_expected_values, 3, my_set_sheet)
        my_set_sheet.insert_missing_columns()
        # Confirm columns with pre-existing values are unchanged
        assert_values_match_those_in_column(col_2_expected_values, 2, my_set_sheet)
        assert_values_match_those_in_column(col_3_expected_values, 3, my_set_sheet)
        poke_column_config = get_poke_columns_config()
        col_config_length = poke_column_config.__len__()
        for i in range(0, col_config_length):
            assert_column_is_in_sheet(poke_column_config[i], my_set_sheet)
        os.remove(excel_copy_path(test_path))

    def test_get_card_numbers_in_sheet(self):
        test_path = "tests/data/test_get_card_numbers_in_sheet.xlsx"
        shutil.copy2(test_path, excel_copy_path(test_path))
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, excel_copy_path(test_path))
        expected_card_numbers = [1, 3, 5, 7, 9]
        actual_card_numbers = my_set_sheet.get_card_numbers_in_sheet()
        assert expected_card_numbers == actual_card_numbers
        os.remove(excel_copy_path(test_path))


def assert_column_is_in_sheet(poke_column: PokeColumn, poke_sheet: PokemonSetSheet):
    if not poke_sheet.is_poke_column_in_columns(poke_column):
        print('\n' + poke_column.__str__() + ' not found in given excel sheet')
    assert poke_sheet.is_poke_column_in_columns(poke_column)


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonSetSheet)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

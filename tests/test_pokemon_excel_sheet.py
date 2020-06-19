import unittest
import unittest.mock as mock
import shutil
import os

from data.models.pokemon_excel_sheet_model import PokeColumn
from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from data.models.pokemon_excel_sheet_model import _get_poke_columns_config
from data.models.pokemon_set_model import PokemonSet
from tests.functions.get_pokemon_test_set import get_pokemon_test_set

base_pokemon_sheet_model_import = 'data.models.pokemon_excel_sheet_model'
get_excel_sheet_import = base_pokemon_sheet_model_import + '._get_excel_workbook_from_file'

test_pokemon_set = get_pokemon_test_set()


class TestPokemonSetSheet(unittest.TestCase):

    @mock.patch(get_excel_sheet_import)
    def test_create_should_call_get_excel_workbook_from_file(self, mock_get_excel_workbook_from_file):
        PokemonSetSheet.create(PokemonSet(None, None, None, None), None)
        assert mock_get_excel_workbook_from_file.called

    def test_should_have_correct_poke_columns(self):
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, 'tests/data/test_pokemon_excel_sheet.xlsx')
        assert my_set_sheet.is_poke_column_in_columns(PokeColumn('Card #', 1))
        assert my_set_sheet.is_poke_column_in_columns(PokeColumn('4 Owned', 2))
        assert my_set_sheet.is_poke_column_in_columns(PokeColumn('CardZ #99 bloppp', 40)) is False

    def test_should_insert_columns_if_missing(self):
        shutil.copy2('tests/data/test_pokemon_excel_sheet.xlsx', 'tests/data/test_pokemon_excel_sheet_copy.xlsx')
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, 'tests/data/test_pokemon_excel_sheet_copy.xlsx')
        my_set_sheet._insert_columns_if_missing()
        poke_column_config = _get_poke_columns_config()
        col_config_length = poke_column_config.__len__()
        for i in range(0, col_config_length):
            assert my_set_sheet.is_poke_column_in_columns(poke_column_config[i])
        my_set_sheet.save()
        os.remove('tests/data/test_pokemon_excel_sheet_copy.xlsx')

    def test_should_have_correct_values(self):
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, 'tests/data/test_pokemon_excel_sheet.xlsx')
        col_1_expected_values = [1, 2, 3, 4]
        col_2_expected_values = ['Yes', 'Yes', 'Yes', 'Yes']
        for i in range(2, 6):
            assert my_set_sheet.excel_sheet.cell(row=i, column=1).value == col_1_expected_values[i - 2]
            assert my_set_sheet.excel_sheet.cell(row=i, column=2).value == col_2_expected_values[i - 2]

    def test_get_missing_metadata_should_save_pokemon_names_to_sheet(self):
        pass


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonSetSheet)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

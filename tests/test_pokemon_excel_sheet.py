import unittest
import unittest.mock as mock
from data.models.pokemon_excel_sheet_model import PokeColumn
from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from tests.functions.get_pokemon_test_set import get_pokemon_test_set

base_pokemon_sheet_model_import = 'data.models.pokemon_excel_sheet_model'
get_excel_sheet_import = base_pokemon_sheet_model_import + '._get_excel_sheet_from_file_by_set'

test_pokemon_set = get_pokemon_test_set()


class TestPokemonSetSheet(unittest.TestCase):

    @mock.patch(get_excel_sheet_import)
    def test_create_should_call_get_excel_sheet_from_file_by_set(self, mock_get_excel_sheet_from_file):
        PokemonSetSheet.create(None, None)
        assert mock_get_excel_sheet_from_file.called

    def test_should_have_correct_poke_columns(self):
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, 'tests/data/test_pokemon_excel_sheet.xlsx')
        assert my_set_sheet.is_poke_column_in_columns(PokeColumn('Card #', 0))
        assert my_set_sheet.is_poke_column_in_columns(PokeColumn('4 Owned', 1))
        assert my_set_sheet.is_poke_column_in_columns(PokeColumn('CardZ #99 bloppp', 40)) is False

    def test_should_have_correct_values(self):
        my_set_sheet = PokemonSetSheet.create(test_pokemon_set, 'tests/data/test_pokemon_excel_sheet.xlsx')
        col_1_expected_values = [1, 2, 3, 4]
        col_2_expected_values = ['Yes', 'Yes', 'Yes', 'Yes']
        for i in range(1, 5):
            assert my_set_sheet.excel_sheet_object.col(0)[i].value == col_1_expected_values[i - 1]
            assert my_set_sheet.excel_sheet_object.col(1)[i].value == col_2_expected_values[i - 1]

    def test_get_missing_metadata_should_save_pokemon_names_to_sheet(self):
        pass


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonSetSheet)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

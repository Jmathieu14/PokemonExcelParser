import unittest
import unittest.mock as mock

import data.models.pokemon_excel_sheet_model as pokemon_excel_sheet_model
from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from data.models.pokemon_set_model import PokemonSet

base_pokemon_sheet_model_import = 'data.models.pokemon_excel_sheet_model'
get_excel_sheet_import = base_pokemon_sheet_model_import + '._get_excel_sheet_from_file_by_set'


class TestPokemonSetSheet(unittest.TestCase):

    @mock.patch(get_excel_sheet_import)
    def test_create_should_call_get_excel_sheet_from_file_by_set(self, mock_get_excel_sheet_from_file):
        PokemonSetSheet.create(None, None)
        assert mock_get_excel_sheet_from_file.called


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonSetSheet)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

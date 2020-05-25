import unittest

from data.models.pokemon_excel_sheet_model import PokemonSetSheetException, PokemonSetSheet
from data.models.pokemon_set_model import PokemonSet


class TestPokemonSetSheet(unittest.TestCase):
    def test_exception_thrown_for_invalid_pokemon_set_input(self):
        with self.assertRaises(PokemonSetSheetException):
            PokemonSetSheet('some invalid pokemon set...', '', 'file_path')

    def test_exception_thrown_for_invalid_excel_sheet_input(self):
        with self.assertRaises(PokemonSetSheetException):
            PokemonSetSheet(PokemonSet('my_abbr', 'my_name', 'my_series'), 'invalid sheet', 'file_path')


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonSetSheet)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

import unittest

from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from data.models.pokemon_set_model import PokemonSet


class TestPokemonSetSheet(unittest.TestCase):
    def test_something(self):
        assert(True == False)


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonSetSheet)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

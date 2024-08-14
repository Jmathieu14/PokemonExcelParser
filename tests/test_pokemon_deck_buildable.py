# Author: Jacques
# Date: 11/21/2021
# Time: 3:37 PM

import unittest
from unittest import mock

from data.functions.pokemon_deck_buildable import is_pokemon_deck_buildable
from data.models.pokemon_card_model import PokemonCard
from data.models.pokemon_deck_item_model import PokemonDeckItem
from data.models.pokemon_deck_summary_model import PokemonDeckSummary
from data.models.pokemon_set_model import PokemonSet


class MockSetSheet:
    def __init__(self):
        pass

    def get_cards_with_name(self, name):
        return name


deck_line_one = "1 Air Balloon SSH 156"
swsh1 = PokemonSet("SSH", "Sword & Shield", "Sword & Shield", "swsh1", False)
deck_line_multiple_cards = "2 Zacian V CEL 16"
cel25 = PokemonSet("CEL", "Celebrations", "Sword & Shield", "cel25", False)
air_balloon = PokemonCard.builder() \
    .name("Air Balloon") \
    .build_index(156) \
    .build_set(swsh1)
air_balloon_deck_item = PokemonDeckItem(item=air_balloon, count=1)
zacian_v = PokemonCard.builder() \
    .name("Zacian V") \
    .build_index(16) \
    .build_set(cel25)
zacian_v_deck_item = PokemonDeckItem(item=zacian_v, count=2)
deck_line_pokemon_summary_text = "Pokemon - 3"
pokemon_summary = PokemonDeckSummary(summary_type="Pokemon", total=3)
pokemon_summary_2 = PokemonDeckSummary(summary_type="Pokemon", total=2)
trainer_summary = PokemonDeckSummary(summary_type="Trainer", total=1)

mock_deck_list = [
    pokemon_summary_2,
    zacian_v_deck_item,
    trainer_summary,
    air_balloon_deck_item
]

mock_poke_set = PokemonSet('CEL', 'Celebrations', 'Sword & Shield', 'cel25', False)


class TestPokemonDeckBuildable(unittest.TestCase):
    @mock.patch('data.functions.pokemon_deck_buildable.decklist_file_to_decklist')
    def test_is_deck_buildable__calls_decklist_file_to_decklist(self, mock_decklist_file_to_decklist):
        is_pokemon_deck_buildable("dummyFilePath.dummy", "mock.excel.path")
        mock_decklist_file_to_decklist.assert_called_once_with("dummyFilePath.dummy")

    @mock.patch('data.functions.pokemon_deck_buildable.get_sets')
    @mock.patch('data.functions.pokemon_deck_buildable.decklist_file_to_decklist')
    def test_is_deck_buildable__calls_get_sets(self, mock_decklist_file_to_decklist, mock_get_sets):
        is_pokemon_deck_buildable("my_mock_path", "mock.excel.path")
        mock_decklist_file_to_decklist.assert_called_once_with("my_mock_path")
        mock_get_sets.assert_called_once()

    @mock.patch('data.functions.pokemon_deck_buildable.find_set_in_sets')
    @mock.patch('data.functions.pokemon_deck_buildable.decklist_file_to_decklist')
    @mock.patch('data.models.pokemon_excel_sheet_model.PokemonSetSheet.create')
    def test_is_deck_buildable__calls_find_set_in_sets(self, mock_create, mock_decklist_file_to_decklist,
                                                       mock_find_set_in_sets):
        mock_decklist_file_to_decklist.return_value = mock_deck_list
        mock_find_set_in_sets.return_value = mock_poke_set
        mock_create.return_value = MockSetSheet()
        is_pokemon_deck_buildable("my_mock_path", "mock.excel.path")
        expected_calls = [
            mock.call("CEL", mock.ANY),
            mock.call("SSH", mock.ANY)]
        mock_find_set_in_sets.assert_has_calls(expected_calls)


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPokemonDeckBuildable)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

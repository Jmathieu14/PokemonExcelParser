import unittest
import utility as util
import simplejson as j
from unittest import mock

from pokemontcgsdk import Set
from data.functions.pokemon_set_list_functions import get_sets
from data.functions.set_pokemon_set_abbreviations_file import add_set_info_to_abbreviations_file
from data.models.pokemon_set_model import PokemonSet
from retrieval.models.pokemon_set_info_response import PokemonSetInfoResponse


DUMMY_SET = Set(id='id', images=None, legalities=None, name='name', printedTotal=100,
                ptcgoCode='ptcgoCode', releaseDate='releaseDate', series='series', total=100, updatedAt='updatedAt')
DUMMY_INFO_RESPONSE = PokemonSetInfoResponse(DUMMY_SET)
INITIAL_POKEMON_SET_ABBREVIATIONS_JSON_STR = '[{"abbreviation": "TEST_SET", "name": "Test Set", "series": "The Test Series!", "set_code": "test1"}]'
TEST_POKEMON_SET_ABBREVIATIONS_JSON_PATH = 'tests/data/test_set_abbreviations_functions_file.json'


class TestSetPokemonSetAbbreviationsFile(unittest.TestCase):
    @mock.patch('utility.json_object_to_file')
    @mock.patch('builtins.print')
    @mock.patch('data.functions.pokemon_set_list_functions.get_sets')
    @mock.patch('data.functions.pokemon_set_list_functions.find_set_in_sets')
    def test_add_set_info_should_print_error_message(self, mock_find_set_in_sets, mock_get_sets, mock_print, mock_save_json_object):
        mock_save_json_object.return_value = None
        mock_get_sets.return_value = []
        mock_find_set_in_sets.return_value = PokemonSet(
            DUMMY_SET.ptcgoCode, DUMMY_SET.name, DUMMY_SET.series, DUMMY_SET.id)
        add_set_info_to_abbreviations_file(DUMMY_INFO_RESPONSE)
        expectedLog = 'Set %s already in pokemon_set_abbreviations.json' % DUMMY_INFO_RESPONSE.ptcgoCode
        assert mock_print.called_once_with(expectedLog)

    @mock.patch('utility.json_object_to_file')
    @mock.patch('builtins.print')
    @mock.patch('data.functions.pokemon_set_list_functions.get_sets')
    @mock.patch('data.functions.pokemon_set_list_functions.find_set_in_sets')
    def test_add_set_info_should_print_adding_set_message(self, mock_find_set_in_sets, mock_get_sets, mock_print, mock_save_json_object):
        mock_save_json_object.return_value = None
        mock_get_sets.return_value = []
        mock_find_set_in_sets.return_value = None
        add_set_info_to_abbreviations_file(DUMMY_INFO_RESPONSE)
        expected_log = 'Adding %s to pokemon_set_abbreviations.json' % DUMMY_INFO_RESPONSE.ptcgoCode
        assert mock_print.called_once_with(expected_log)

    @mock.patch('data.functions.pokemon_set_list_functions.get_pokemon_set_abbreviations_file_path')
    @mock.patch('data.functions.set_pokemon_set_abbreviations_file.get_pokemon_set_abbreviations_file_path')
    def test_add_set_info_adds_set_to_json_file(self, mock_get_pokemon_set_abbreviations_file_path_local, mock_get_pokemon_set_abbreviations_file_path_external):
        mock_get_pokemon_set_abbreviations_file_path_local.return_value = TEST_POKEMON_SET_ABBREVIATIONS_JSON_PATH
        mock_get_pokemon_set_abbreviations_file_path_external.return_value = TEST_POKEMON_SET_ABBREVIATIONS_JSON_PATH
        util.json_object_to_file(j.loads(
            INITIAL_POKEMON_SET_ABBREVIATIONS_JSON_STR), TEST_POKEMON_SET_ABBREVIATIONS_JSON_PATH)
        assert get_sets().__len__() == 1
        add_set_info_to_abbreviations_file(DUMMY_INFO_RESPONSE)
        assert get_sets().__len__() == 2


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestSetPokemonSetAbbreviationsFile)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()

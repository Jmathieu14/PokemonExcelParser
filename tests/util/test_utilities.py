# Author: Jacques
# Date: 06/07/2020
# Time: 10:45 PM
from data.models.pokemon_card_model import SimplerCard
from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from data.models.pokemon_set_model import PokemonSet
from retrieval.models.index_card_model import IndexCard

from unittest.mock import Mock
from typing import Optional
import utility as util


# Mock the pokemontcgsdk Set
class MockSet:
    id: str
    name: str
    ptcgoCode: Optional[str]
    releaseDate: str
    series: str
    total: int
    legalities: any

    def __init__(self, id_str, total: int, name, ptcgo_code, release_date, series):
        self.id = id_str
        self.total = total
        self.name = name
        self.ptcgoCode = ptcgo_code
        self.releaseDate = release_date
        self.series = series
        self.legalities = {
            "unlimited": "Legal"
        }


    def __str__(self):
        return "{{ 'id': '{0}'," \
            "'total': '{1}'," \
            "'name': '{2}'," \
            "'ptcgoCode': '{3}'," \
            "'releaseDate': '{4}'," \
            "'series': '{5}'," \
            "'legalities': '{6}' }}" \
            .format(self.id, self.total, self.name, self.ptcgoCode, self.releaseDate, self.series, self.legalities)


def makeDummySet(total_cards: int) -> MockSet:
    return MockSet('dummy', total_cards, 'dummy', 'dummy', 'dummy', 'dummy')


def get_pokemon_test_set():
    return PokemonSet.json_to_pokemon_set(util.file_to_json_obj('tests/data/test_set_abbreviations.json')[0])


def excel_copy_path(path: str):
    return path.split('.')[0] + '_copy.xlsx'


def empty_index_card():
    return IndexCard(0, SimplerCard.init_empty())


def index_card(index: int, name: str, rarity: str, _type: str):
    card: SimplerCard = SimplerCard.init_empty()
    card.name = name
    card.rarity = rarity
    card.types = [_type]
    return IndexCard(index, card)


def assert_values_match_those_in_column(values: [], column_index: int, poke_sheet: PokemonSetSheet):
    values_length = values.__len__()
    for i in range(2, values_length + 2):
        poke_sheet_value = poke_sheet.excel_sheet.cell(row=i, column=column_index).value
        if not poke_sheet_value == values[i - 2]:
            print("\nThe value '{0}' at row {1}, column {2} does not match the expected cell value of '{3}'".format(
                    poke_sheet_value,
                    i, column_index,
                    values[i - 2]))
        assert poke_sheet_value == values[i - 2]


# Source 1 (see bottom)
def assert_not_called_with(self, *args, **kwargs):
    try:
        self.assert_called_with(*args, **kwargs)
    except AssertionError:
        return
    raise AssertionError('Expected %s to not have been called.' % self._format_mock_call_signature(args, kwargs))


# Make sure to add the following line in your test files
Mock.assert_not_called_with = assert_not_called_with


# Source 1: credit for function definition goes to 'blhsing' for StackOverflow post:
# www.stackoverflow.com/questions/54838354/python-how-can-i-assert-a-mock-object-was-not-called-with-specific-argument
# User profile: https://stackoverflow.com/users/6890912/blhsing

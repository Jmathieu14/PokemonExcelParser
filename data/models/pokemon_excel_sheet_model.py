from data.models.pokemon_set_model import PokemonSet
import excelrd
import openpyxl
from openpyxl import worksheet
from openpyxl import workbook


class PokeColumn:
    def __init__(self, name: str, preferred_index: int):
        self.name = name
        self.index = preferred_index

    def column_name_matches(self, other_poke_column):
        return self.name.lower() == other_poke_column.name.lower()

    def equals(self, other_poke_column):
        return self.column_name_matches(other_poke_column) and self.index == other_poke_column.index


def _get_poke_columns_config():
    return [PokeColumn('Card #', 2),
            PokeColumn('4 Owned', 3),
            PokeColumn('Name', 1),
            PokeColumn('Rarity', 4)]


def _get_excel_workbook_from_file(pokemon_set: PokemonSet, file_path: str) -> workbook:
    return openpyxl.load_workbook(file_path)


class PokemonSetSheet:
    def __init__(self, pokemon_set: PokemonSet, excel_workbook: workbook, excel_sheet: worksheet, file_path: str):
        self.pokemon_set = pokemon_set
        self.excel_workbook: openpyxl.workbook = excel_workbook
        self.excel_sheet: worksheet = excel_sheet
        self.file_path = file_path
        # List of type PokeColumn

    def is_poke_column_in_columns(self, poke_column: PokeColumn):
        for i in range(1, self.excel_sheet.max_column + 1):
            my_column = PokeColumn(self.excel_sheet.cell(row=1, column=i).value, i)
            if poke_column.equals(my_column):
                return True
        return False

    def is_column_empty(self, column_index):
        for i in range(2, self.excel_sheet.max_row + 1):
            if self.excel_sheet.cell(row=i, column=column_index).value is not None:
                return False
        return True

    def insert_column(self, poke_column: PokeColumn):
        # check if cells below header of column have values
        if not self.is_column_empty(poke_column.index):
            # if not and the poke_column being inserted has a diff name, move the existing column to end of column list
            print('not empty! ')
        else:
            print('before - ' + str(self.excel_sheet.cell(row=1, column=poke_column.index).value))
            self.excel_sheet.cell(row=1, column=poke_column.index).value = poke_column.name
            print('after - ' + str(self.excel_sheet.cell(row=1, column=poke_column.index).value))

    def _insert_columns_if_missing(self):
        column_config = _get_poke_columns_config()
        for i in range(0, column_config.__len__()):
            my_col: PokeColumn = column_config[i]
            if not self.is_poke_column_in_columns(my_col):
                self.insert_column(my_col)

    def save(self):
        self.excel_workbook.save(self.file_path)

    def create(pokemon_set: PokemonSet, file_path: str):
        excel_workbook = _get_excel_workbook_from_file(pokemon_set, file_path)
        excel_sheet = excel_workbook.get_sheet_by_name(pokemon_set.abbreviation)
        return PokemonSetSheet(pokemon_set, excel_workbook, excel_sheet, file_path)

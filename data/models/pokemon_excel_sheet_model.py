from data.models.pokemon_set_model import PokemonSet
import excelrd
import openpyxl
from openpyxl import worksheet
from openpyxl import workbook

DEBUG_MODE = False


class PokeColumn:
    def __init__(self, name: str, preferred_index: int):
        self.name = '' if name is None else name
        self.index = preferred_index

    def column_name_matches(self, other_poke_column):
        return self.name.lower() == other_poke_column.name.lower()

    def equals(self, other_poke_column):
        return self.column_name_matches(other_poke_column) and self.index == other_poke_column.index


def get_poke_columns_config():
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
        self.column_config = get_poke_columns_config()
        self.__column_offset__ = self.column_config.__len__() + self.excel_sheet.max_column
        self.configure_columns()

    def _move_column_from_index_to_other_index(self, index, other_index):
        values_to_move = []
        for i in range(1, self.excel_sheet.max_row + 1):
            values_to_move.append(self.excel_sheet.cell(row=i, column=index).value)
            self.excel_sheet.cell(row=i, column=index).value = ''

        for j in range(1, self.excel_sheet.max_row + 1):
            self.excel_sheet.cell(row=j, column=other_index).value = values_to_move[j-1]

    def is_poke_column_in_columns(self, poke_column: PokeColumn):
        for i in range(1, self.excel_sheet.max_column + 1):
            my_column = PokeColumn(self.excel_sheet.cell(row=1, column=i).value, i)
            if poke_column.equals(my_column):
                return True
        return False

    def get_index_of_column_with_name(self, column_name):
        for i in range(1, self.excel_sheet.max_column + 1):
            name_at_i = self.excel_sheet.cell(row=1, column=i).value
            if name_at_i == column_name:
                return i
        return -1

    def is_column_empty(self, column_index):
        for i in range(2, self.excel_sheet.max_row + 1):
            if self.excel_sheet.cell(row=i, column=column_index).value is not None:
                return False
        return True

    def configure_columns(self):
        if not DEBUG_MODE:
            self.move_existing_columns_out_of_way()
            self.move_existing_columns_to_proper_index()
            self.insert_missing_columns()

    def insert_column(self, poke_column: PokeColumn):
        # check if cells below header of column have values
        if not self.is_column_empty(poke_column.index):
            # if not and the poke_column being inserted has a diff name, move the existing column to end of column list
            print('not empty! ')
            self.move_entire_column_from_index_to_end(poke_column.index)
            # self.insert_column(poke_column)
        else:
            print('before - ' + str(self.excel_sheet.cell(row=1, column=poke_column.index).value))
            self.excel_sheet.cell(row=1, column=poke_column.index).value = poke_column.name
            print('after - ' + str(self.excel_sheet.cell(row=1, column=poke_column.index).value))

    def insert_missing_columns(self):
        pass

    def move_existing_columns_to_proper_index(self):
        for i in range(0, self.column_config.__len__()):
            config_col: PokeColumn = self.column_config[i]
            existing_col_index = self.get_index_of_column_with_name(config_col.name)
            if existing_col_index != -1:
                self._move_column_from_index_to_other_index(existing_col_index, config_col.index)

    def move_existing_columns_out_of_way(self):
        last_column = self.excel_sheet.max_column + 1
        for i in range(1, last_column):
            if not self.is_column_empty(i):
                self._move_column_from_index_to_other_index(i, i + self.__column_offset__)

    def save(self):
        self.excel_workbook.save(self.file_path)

    def create(pokemon_set: PokemonSet, file_path: str):
        excel_workbook = _get_excel_workbook_from_file(pokemon_set, file_path)
        excel_sheet = excel_workbook.get_sheet_by_name(pokemon_set.abbreviation)
        return PokemonSetSheet(pokemon_set, excel_workbook, excel_sheet, file_path)

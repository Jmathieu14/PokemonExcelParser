from itertools import count

from data.models.pokemon_set_model import PokemonSet
import excelrd


class PokeColumn:
    def __init__(self, name: str, preferred_index: int):
        self.name = name
        self.index = preferred_index

    def column_name_matches(self, other_poke_column):
        return self.name.lower() == other_poke_column.name.lower()

    def equals(self, other_poke_column):
        return self.column_name_matches(other_poke_column) and self.index == other_poke_column.index


def _get_poke_columns_config():
    return [PokeColumn('Card #', 1),
            PokeColumn('4 Owned', 2),
            PokeColumn('Name', 0),
            PokeColumn('Rarity', 3)]


def _get_excel_sheet_from_file_by_set(pokemon_set: PokemonSet, file_path: str) -> excelrd.sheet.Sheet:
    workbook = excelrd.open_workbook(file_path)
    return workbook.sheet_by_name(pokemon_set.abbreviation)


class PokemonSetSheet:
    def __init__(self, pokemon_set: PokemonSet, excel_sheet_object: excelrd.sheet.Sheet, file_path: str):
        self.pokemon_set = pokemon_set
        self.excel_sheet_object = excel_sheet_object
        self.file_path = file_path
        # List of type PokeColumn
        self.columns = []
        self.configure_columns()

    def is_poke_column_in_columns(self, poke_column: PokeColumn):
        for col in self.columns:
            if poke_column.equals(col):
                return True
        return False

    def insert_missing_columns(self):
        pass

    def reorder_columns(self):
        excel_columns = self.excel_sheet_object.col

    def configure_columns(self):
        if self.excel_sheet_object is not None:
            excel_columns_count = self.excel_sheet_object.ncols
            for i in range(0, self.excel_sheet_object.ncols):
                col_name = self.excel_sheet_object.col(i)[0].value
                self.columns.append(PokeColumn(col_name, i))

    def create(pokemon_set: PokemonSet, file_path: str):
        excel_sheet_object = _get_excel_sheet_from_file_by_set(pokemon_set, file_path)
        return PokemonSetSheet(pokemon_set, excel_sheet_object, file_path)

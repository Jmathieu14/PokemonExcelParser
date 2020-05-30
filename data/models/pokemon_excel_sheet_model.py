from itertools import count

from data.models.pokemon_set_model import PokemonSet
import excelrd


def _get_excel_sheet_from_file_by_set(pokemon_set: PokemonSet, file_path: str) -> excelrd.sheet.Sheet:
    workbook = excelrd.open_workbook(file_path)
    return workbook.sheet_by_name(pokemon_set.abbreviation)


class PokeColumn:
    def __init__(self, name: str, preferred_index: int):
        self.name = name
        self.preferred_index = preferred_index


class PokemonSetSheet:
    def __init__(self, pokemon_set: PokemonSet, excel_sheet_object: excelrd.sheet.Sheet, file_path: str):
        self.pokemon_set = pokemon_set
        self.excel_sheet_object = excel_sheet_object
        self.file_path = file_path
        self.column_names = [PokeColumn('Card #', 1),
                             PokeColumn('4 Owned', 2),
                             PokeColumn('Name', 0),
                             PokeColumn('Rarity', 3)]
        self.configure_columns()

    def insert_missing_columns(self):
        pass

    def reorder_columns(self):
        excel_columns = self.excel_sheet_object.col

    def configure_columns(self):
        excel_columns_count = self.excel_sheet_object.ncols
        if excel_columns_count < self.column_names.__len__():
            self.insert_missing_columns()
        self.reorder_columns()

    def create(pokemon_set: PokemonSet, file_path: str):
        excel_sheet_object = _get_excel_sheet_from_file_by_set(pokemon_set, file_path)
        return PokemonSetSheet(pokemon_set, excel_sheet_object, file_path)

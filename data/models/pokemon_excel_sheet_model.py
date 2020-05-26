from data.models.pokemon_set_model import PokemonSet
import os.path as osp
import excelrd


def _get_excel_sheet_from_file_by_set(pokemon_set: PokemonSet, file_path: str):
    workbook = excelrd.open_workbook(file_path)
    return workbook.sheet_by_name(pokemon_set.abbreviation)


class PokemonSetSheet:
    def __init__(self, pokemon_set: PokemonSet, excel_sheet_object: excelrd.sheet.Sheet, file_path: str):
        self.pokemon_set = pokemon_set
        self.excel_sheet_object = excel_sheet_object
        self.file_path = file_path

    def create(pokemon_set: PokemonSet, file_path: str):
        excel_sheet_object = _get_excel_sheet_from_file_by_set(pokemon_set, file_path)
        return PokemonSetSheet(pokemon_set, excel_sheet_object, file_path)

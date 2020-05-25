from data.models.pokemon_set_model import PokemonSet
import os.path as osp
import excelrd


class PokemonSetSheetException(Exception):
    def __init__(self, message):
        self.message = message


def _validate_input(pokemon_set, excel_sheet_object, file_path):
    if not isinstance(pokemon_set, PokemonSet):
        raise PokemonSetSheetException("PokemonSet was expected for 'pokemon_set'; was instead given [{}] of type [{}]"
                                       .format(pokemon_set, type(pokemon_set)))
        return False
    if not isinstance(excel_sheet_object, type(excelrd.sheet)):
        raise PokemonSetSheetException("excelrd.sheet was expected for 'excel_sheet_object'; was instead given [{}] "
                                       "of type [{}]"
                                       .format(excel_sheet_object, type(excel_sheet_object)))
        return False
    if not isinstance(str, file_path) or not isinstance(osp, file_path):
        raise PokemonSetSheetException("str was expected for 'file_path'; was instead given [{}] of type [{}]"
                                       .format(file_path, type(file_path)))
        return False
    return True


class PokemonSetSheet:
    def __init__(self, pokemon_set, excel_sheet_object, file_path):
        if _validate_input(pokemon_set, excel_sheet_object, file_path):
            self.pokemon_set = pokemon_set
            self.excel_sheet_object = excel_sheet_object
            self.file_path = file_path

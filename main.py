import shutil
import sys

from data.functions.pokemon_excel_sheet_functions import update_missing_pokemon_metadata, insert_complete_set_metadata, \
    add_conditional_formatting_from_config
from data.functions.pokemon_set_list_functions import get_sets, find_set_in_sets
from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from utility import backup_excel_sheet_filename, remove_backup, file_exists

ALL_SETS = get_sets()


def get_excel_file_path():
    excel_file_path = 'C:\\Users\\User\\OneDrive\\Pokemon TCG Cards Owned.xlsx'
    alternate_excel_file_path = 'C:\\Users\\jmath\\OneDrive\\Pokemon TCG Cards Owned.xlsx'
    if not file_exists(excel_file_path) and file_exists(alternate_excel_file_path):
        excel_file_path = alternate_excel_file_path
    return excel_file_path


def insert_complete_set_data(my_pokemon_sheet: PokemonSetSheet):
    insert_complete_set_metadata(my_pokemon_sheet)


def update_excel_sheet(set_abbr: str, get_complete_set_info=False):
    my_set = find_set_in_sets(set_abbr, ALL_SETS)
    excel_file_path = get_excel_file_path()
    # Remove previous back-up if existing
    remove_backup(excel_file_path)
    # Make back-up file for user
    shutil.copy2(excel_file_path, backup_excel_sheet_filename(excel_file_path))
    my_pokemon_sheet = PokemonSetSheet.create(my_set, excel_file_path)
    my_pokemon_sheet.save()
    update_missing_pokemon_metadata(my_pokemon_sheet)
    if get_complete_set_info:
        insert_complete_set_data(my_pokemon_sheet)
    my_pokemon_sheet.save()


def update_excel_sheets(set_abbreviations: [], get_complete_set_info=False):
    for poke_set in set_abbreviations:
        update_excel_sheet(poke_set, get_complete_set_info)


def main(argv):
    if argv.__contains__("test"):
        print("Testing out functions... TODO: keep log of sheets with conditional formatting already applied")
        my_set = find_set_in_sets("CPA", ALL_SETS)
        excel_file_path = get_excel_file_path()
        shutil.copy2(excel_file_path, backup_excel_sheet_filename(excel_file_path))
        my_pokemon_set_sheet = PokemonSetSheet.create(my_set, excel_file_path)
        add_conditional_formatting_from_config(my_pokemon_set_sheet)
        my_pokemon_set_sheet.save()
    else:
        sets_to_update = ['SSH', 'CPA', 'DAA', 'VIV', 'CRE', 'EVS', 'BST', 'CEL', 'PR-SW', 'SHF', 'FST']
        update_excel_sheets(sets_to_update, get_complete_set_info=False)


if __name__ == '__main__':
    main(sys.argv[1:])

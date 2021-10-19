import shutil
import sys

from data.functions.pokemon_excel_sheet_functions import update_missing_pokemon_metadata, insert_complete_set_metadata
from data.functions.pokemon_set_list_functions import get_sets, find_set_in_sets
from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from utility import backup_excel_sheet_filename, remove_backup, file_exists


# TODO: prevent pokemon tcg api from calling card.find on secret type cards

def main(argv):
    sets_to_update = ['SSH', 'CPA', 'DAA', 'VIV', 'CRE', 'EVS', 'BST', 'CEL', 'PR-SW']
    for poke_set in sets_to_update:
        update_excel_sheet(poke_set, get_complete_set_info=False)


def update_excel_sheet(set_abbr: str, get_complete_set_info=False):
    my_sets = get_sets()
    my_set = find_set_in_sets(set_abbr, my_sets)
    excel_file_path = 'C:\\Users\\User\\OneDrive\\Pokemon TCG Cards Owned.xlsx'
    alternate_excel_file_path = 'C:\\Users\\jmath\\OneDrive\\Pokemon TCG Cards Owned.xlsx'
    if not file_exists(excel_file_path) and file_exists(alternate_excel_file_path):
        excel_file_path = alternate_excel_file_path
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


def insert_complete_set_data(my_pokemon_sheet: PokemonSetSheet):
    insert_complete_set_metadata(my_pokemon_sheet)


if __name__ == '__main__':
    main(sys.argv[1:])

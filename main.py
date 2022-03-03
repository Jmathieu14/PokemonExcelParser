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
    caps_argv = []
    for i in range(0, argv.__len__()):
        caps_argv.append(argv[i].upper())
    if caps_argv.__contains__("HELP"):
        print("\nCommand Format: `python main.py <OPTIONS>`\n")
        print("Options:\n")
        print("- Set Abbreviations - update pokemon owned spreadsheet per the set specified (i.e. CEL)")
        print("- SETS - show all sets that can be updated")
        print("- APPLY_FORMATTING - applies formatting to sets specified in main.py")
        print("- HELP, H - bring up the help menu\n")
    elif argv.__contains__("APPLY_FORMATTING"):
        print("TODO: keep log of sheets with conditional formatting already applied to avoid appending duplicate rules")
        # Temp log of sets with existing formatting: FLI - FST
        excel_file_path = get_excel_file_path()
        shutil.copy2(excel_file_path, backup_excel_sheet_filename(excel_file_path))
        sets_to_update = []
        for i in range(0, sets_to_update.__len__()):
            my_set = find_set_in_sets(sets_to_update[i], ALL_SETS)
            print('Found set %s' % sets_to_update[i])
            my_set.print()
            print('Creating PokemonSetSheet with %s at the path: %s' % (sets_to_update[i], excel_file_path))
            my_pokemon_set_sheet = PokemonSetSheet.create(my_set, excel_file_path)
            print('Adding config...')
            add_conditional_formatting_from_config(my_pokemon_set_sheet)
            print('Saving changes...')
            my_pokemon_set_sheet.save()
            print('Conditional Formatting Applied to: %s' % sets_to_update[i])
    elif caps_argv.__contains__("SETS"):
        sets_availabe = ['SSH', 'CPA', 'DAA', 'VIV', 'CRE', 'EVS', 'BST', 'CEL', 'PR-SW', 'SHF', 'FST', 'BRS']
        print(sets_availabe)
    else:
        sets_to_update = caps_argv
        print("\nUpdating the following set(s): ")
        print(sets_to_update)
        if sets_to_update.__len__() > 0:
            update_excel_sheets(sets_to_update, get_complete_set_info=False)


if __name__ == '__main__':
    main(sys.argv[1:])

import shutil
import sys

from data.functions.pokemon_deck_buildable import is_pokemon_deck_buildable
from data.functions.pokemon_deck_functions import decklist_file_to_decklist
from data.functions.pokemon_excel_sheet_functions import update_missing_pokemon_metadata, insert_complete_set_metadata, \
    add_conditional_formatting_from_config
from data.functions.pokemon_set_list_functions import get_sets, find_set_in_sets
from data.functions.set_pokemon_set_abbreviations_file import add_set_info_to_abbreviations_file, add_sets_to_abbreviations_file
from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from data.models.pokemon_set_model import create_dummy_set_from_set_code
from retrieval.pokemon_tcg_api import get_latest_standard_sets, get_set_info
from retrieval.auth import init_api_auth
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
        if argv[i][0] == "-":
            caps_argv.append(argv[i].upper().replace("-", ""))
        else:
            caps_argv.append(argv[i].upper())
    if caps_argv.__contains__("HELP") or caps_argv.__contains__("H") or caps_argv.__len__() == 0:
        print("\nCommand Format: `python main.py <OPTIONS>`\n")
        print("Options:\n")
        print("- Set Abbreviations - update pokemon owned spreadsheet per the set specified (i.e. CEL)")
        print("- SETS <OPTIONS> - show all sets that can be updated")
        print("\tOptions:")
        print("\t  - UPDATE - update any missing set information to the set abbreviations config file")
        print("\t  - LATEST - show all latest standard legal sets")
        print("- SET_INFO <set> <OPTIONS> - get information for specified set using pokemontcgsdk 'set_code'")
        print("\tOptions:")
        print("\t  - ADD - add the specified set information to the set abbreviations config file")
        print("- APPLY_FORMATTING - applies formatting to sets specified in main.py")
        print("- DEV <command> - runs a dev command to test it's functionality")
        print("- PARSE_DECK <file> - Parse and print the resulting cards in a given decklist file")
        print("- IS_DECK_BUILDABLE <file> - Parse a decklist file and print if it is buildable")
        print("- HELP, H - bring up the help menu\n")
    elif caps_argv.__contains__("DEV") and caps_argv.__contains__("IS_DECK_BUILDABLE"):
        if caps_argv.__len__() <= 2:
            print("Please pass in the deck list filepath as the third argument")
        else:
            deck_file_path = argv[2]
            print(deck_file_path)
            is_pokemon_deck_buildable(deck_file_path, get_excel_file_path())
    elif caps_argv.__contains__("SET_INFO"):
        my_set = create_dummy_set_from_set_code(str(argv[1]).lower())
        init_api_auth()
        tcg_api_response = get_set_info(my_set)
        if caps_argv.__len__() > 2 and 'ADD' in caps_argv[2]:
            add_set_info_to_abbreviations_file(tcg_api_response)
        print(tcg_api_response)
    elif caps_argv.__contains__("APPLY_FORMATTING"):
        print("TODO: keep log of sheets with conditional formatting already applied to avoid appending duplicate rules")
        # Temp log of sets with existing formatting: FLI - CRZGG
        excel_file_path = get_excel_file_path()
        shutil.copy2(excel_file_path,
                     backup_excel_sheet_filename(excel_file_path))
        sets_to_update = []
        init_api_auth()
        for i in range(0, sets_to_update.__len__()):
            my_set = find_set_in_sets(sets_to_update[i], ALL_SETS)
            print('Found set %s' % sets_to_update[i])
            my_set.print()
            print('Creating PokemonSetSheet with %s at the path: %s' %
                  (sets_to_update[i], excel_file_path))
            my_pokemon_set_sheet = PokemonSetSheet.create(
                my_set, excel_file_path)
            print('Adding config...')
            add_conditional_formatting_from_config(my_pokemon_set_sheet)
            print('Saving changes...')
            my_pokemon_set_sheet.save()
            print('Conditional Formatting Applied to: %s' % sets_to_update[i])
    elif caps_argv.__contains__("SETS"):
        init_api_auth()
        if str(argv[1]).upper() == "--UPDATE":
            latest_sets = get_latest_standard_sets()
            add_sets_to_abbreviations_file(latest_sets)
        elif str(argv[1].upper() == "--LATEST"):
            latest_sets = get_latest_standard_sets()
            for set in latest_sets:
                print(str(set))
        else:
            sets_availabe = ['ASR', 'ASRTG', 'CRE', 'EVS', 'BST', 'CEL', 'PR-SW',
                            'SHF', 'SHFSV', 'FST', 'BRS', 'LOR', 'SVP', 'SV1', 'PAL', 'OBF', 'MEW']
            print(sets_availabe)
    elif caps_argv.__contains__("PARSE_DECK"):
        decklist_filepath = argv[1]
        decklist_object = decklist_file_to_decklist(decklist_filepath)
        decklist_as_string = ''
        for i in range(0, decklist_object.__len__()):
            if i != 0:
                decklist_as_string += ', '
            decklist_as_string += '\n' + decklist_object[i].__str__()
        print(decklist_as_string)
    elif caps_argv.__contains__("IS_DECK_BUILDABLE"):
        deck_file_path = argv[1]
        print(deck_file_path)
        is_pokemon_deck_buildable(deck_file_path, get_excel_file_path())
    else:
        sets_to_update = caps_argv
        print("\nUpdating the following set(s): ")
        print(sets_to_update)
        if sets_to_update.__len__() > 0:
            update_excel_sheets(sets_to_update, get_complete_set_info=False)


if __name__ == '__main__':
    main(sys.argv[1:])

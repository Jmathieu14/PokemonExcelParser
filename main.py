from data.functions.pokemon_set_list_functions import get_sets, find_set_in_sets
from data.models.pokemon_excel_sheet_model import PokemonSetSheet
from data.models.pokemon_set_model import PokemonSet


def main():
    my_sets = get_sets()
    PokemonSet.print_list(my_sets)
    my_set = find_set_in_sets('RCL', my_sets)
    excel_file_path = 'C:\\Users\\User\\OneDrive\\Pokemon TCG Cards Owned.xlsx'
    my_pokemon_sheet = PokemonSetSheet.create(my_set, excel_file_path)
    print(my_pokemon_sheet.excel_sheet_object)
    col_ct = my_pokemon_sheet.excel_sheet_object.ncols
    print('column count: ' + str(col_ct))
    for i in range(0, col_ct):
        print('column name: ' + str(my_pokemon_sheet.excel_sheet_object.col(i)[0].value))


if __name__ == '__main__':
    main()

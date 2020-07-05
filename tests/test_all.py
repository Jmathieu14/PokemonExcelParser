# Author: Jacques
# Date: 05/24/2020
# Time: 9:11 PM
from tests import test_pokemon_excel_sheet, test_pokemon_tcg_api, test_pokemon_excel_sheet_functions


def main():
    test_pokemon_excel_sheet.main()
    test_pokemon_tcg_api.main()
    test_pokemon_excel_sheet_functions.main()


if __name__ == '__main__':
    main()

# Author: Jacques
# Date: 08/28/2020
# Time: 4:15 PM
import getopt
import sys

from data.functions.pokemon_set_list_functions import get_sets, find_set_in_sets
from data.models.pokemon_set_model import create_dummy_set_from_set_code
from retrieval.pokemon_tcg_api import get_set_info
from auth import init_api_auth

GET_SET_INFO = 'get_set_info'
GET_SET_TOTAL = 'get_set_total'


def main(argv):
    init_api_auth()
    if argv.__contains__(GET_SET_INFO):
        try:
            opts, args = getopt.getopt(argv[1:], 's:')
        except getopt.GetoptError as err:
            print(err)
            sys.exit(2)
        for opt, arg in opts:
            set_arg_uppercase = str(arg).upper()
            my_set = find_set_in_sets(set_arg_uppercase, get_sets())
            if my_set is None:
                my_set = create_dummy_set_from_set_code(str(arg).lower())
            tcg_api_response = get_set_info(my_set)
            print(tcg_api_response)
    else:
        print('No function specified')


if __name__ == '__main__':
    main(sys.argv[1:])

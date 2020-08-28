# Author: Jacques
# Date: 08/28/2020
# Time: 4:15 PM
import getopt
import sys

from data.functions.pokemon_set_list_functions import get_sets, find_set_in_sets
from retrieval.pokemon_tcg_api import get_set_info

GET_SET_INFO = 'get_set_info'
GET_SET_TOTAL = 'get_set_total'


def main(argv):
    if argv.__contains__(GET_SET_INFO):
        try:
            opts, args = getopt.getopt(argv[1:], 's:')
        except getopt.GetoptError as err:
            print(err)
            sys.exit(2)
        for opt, arg in opts:
            set_arg_uppercase = str(arg).upper()
            my_set = find_set_in_sets(set_arg_uppercase, get_sets())
            tcg_api_response = get_set_info(my_set)
            print(tcg_api_response)
    else:
        print('No function specified')


if __name__ == '__main__':
    main(sys.argv[1:])

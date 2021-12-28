# Author: Jacques
# Date: 12/28/2021
# Time: 1:37 PM
import string


def column_number_to_letter(index: int):
    letters = list(string.ascii_uppercase)
    return letters[index - 1]

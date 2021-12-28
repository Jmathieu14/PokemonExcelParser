# Author: Jacques
# Date: 12/28/2021
# Time: 12:04 PM
from openpyxl.worksheet import worksheet
from openpyxl.styles import Color, PatternFill, Font, Border, Side
from openpyxl.formatting.rule import FormulaRule
from data.poke_column_config import get_poke_columns_config
from data.utility import column_number_to_letter

COLUMNS = get_poke_columns_config()


def make_formula_text(column_letter: str, energy_type: str):
    return '=($%s1="%s")' % (column_letter, energy_type.capitalize())


def get_energy_type_column_letter():
    for column in COLUMNS:
        if column.name == 'Type':
            return column_number_to_letter(column.index)


def get_applies_to_all_rows():
    last_column = 0
    for column in COLUMNS:
        last_column = max(last_column, column.index)
    last_column_letter = column_number_to_letter(last_column)
    return '$A2:$%s500' % last_column_letter
    # return HashableCellRange(min_col=1, max_col=last_column, min_row=2, max_row=500)


ENERGY_TYPE_COLUMN_LETTER = get_energy_type_column_letter()
APPLIES_TO_ALL_ROWS = get_applies_to_all_rows()

FIRE_FILL = PatternFill(bgColor='FBD1D1', fill_type='solid')
FIRE_BORDER_COLOR = Color('F75F5F', type='hex')
FIRE_BORDER_SIDE = Side(style='medium', color=FIRE_BORDER_COLOR, border_style='thin')
FIRE_BORDER = Border(left=FIRE_BORDER_SIDE,
                     right=FIRE_BORDER_SIDE,
                     top=FIRE_BORDER_SIDE,
                     bottom=FIRE_BORDER_SIDE)
FIRE_FORMULA_TEXT = make_formula_text(ENERGY_TYPE_COLUMN_LETTER, 'Fire')

FIRE_FORMULA = FormulaRule(formula=[FIRE_FORMULA_TEXT], border=FIRE_BORDER, fill=FIRE_FILL)


def add_all_formatting_rules_to_sheet(ws: worksheet):
    ws.conditional_formatting.add(APPLIES_TO_ALL_ROWS, FIRE_FORMULA)


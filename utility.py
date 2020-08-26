import os
import os.path as osp
import simplejson as j


def file_to_json_obj(filename):
    with open(filename, 'r') as my_file:
        my_str = my_file.read()
    my_in = j.loads(my_str)
    return my_in


def remove_backup(filename):
    backup_filename = backup_excel_sheet_filename(filename)
    if osp.exists(backup_filename):
        os.remove(backup_filename)


def backup_excel_sheet_filename(filename):
    return filename.split('.')[0] + '_backup.xlsx'

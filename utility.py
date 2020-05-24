import os.path as osp
import os
import simplejson as j


def file_to_json_obj(filename):
    with open(filename, 'r') as my_file:
        my_str = my_file.read()
    my_in = j.loads(my_str)
    return my_in

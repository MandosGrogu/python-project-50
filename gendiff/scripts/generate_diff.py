import os
from json import load as json_load
from yaml import CLoader
from yaml import load as yml_load


APPROPRIATE_FILE_FORMATS = {
    'yaml': 'yml',
    'yml': 'yml',
    'json': 'json'
}

def read_file_acc_to_format(f):

    file_format = f.split('.')[-1]
    if file_format.lower() in APPROPRIATE_FILE_FORMATS.keys():
        file_format = APPROPRIATE_FILE_FORMATS[file_format]

    if file_format == 'json':
        file = json_load(open(f))
    elif file_format == 'yml':
        file = yml_load(open(f), Loader=CLoader)
    return file

def generate_diff(f1, f2):

    file1 = read_file_acc_to_format(f1)
    sorted_file1 = dict(sorted(file1.items()))

    file2 = read_file_acc_to_format(f2)
    sorted_file2 = dict(sorted(file2.items()))

    result_str = ''

    dict1_keys = [k for k in sorted_file1.keys()]
    dict2_keys = [k for k in sorted_file2.keys()]

    all_keys_list = list(dict.fromkeys(dict1_keys + dict2_keys))

    for k in all_keys_list:
        if k in sorted_file1.keys() and k in sorted_file2.keys():
            if sorted_file2[k] == sorted_file1[k]:
                result_str += f'  {k}: {sorted_file2[k]}{os.linesep}'
            else:
                result_str += f'- {k}: {sorted_file1[k]}{os.linesep}'
                result_str += f'+ {k}: {sorted_file2[k]}{os.linesep}'
        elif k in sorted_file1.keys() and k not in sorted_file2.keys():
            result_str += f'- {k}: {sorted_file1[k]}{os.linesep}'
        else:
            result_str += f'+ {k}: {sorted_file2[k]}{os.linesep}'

    return result_str
import json
import os
from argparse import ArgumentParser


def main():

    parser = ArgumentParser(
        prog='gendiff', 
        usage='%(prog)s [-h] [-f FORMAT] first_file second_file', 
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', nargs='+')
    parser.add_argument('second_file', nargs='+')
    parser.add_argument('-f FORMAT', 
        '--format FORMAT', nargs='?', 
        help='set format of output')

    args = parser.parse_args()
    print(args)

    if args.first_file and args.second_file:
        return generate_diff(args.first_file[0], args.second_file[0])


def generate_diff(f1, f2):

    file1 = json.load(open(f1))
    sorted_file1 = dict(sorted(file1.items()))

    file2 = json.load(open(f2))
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


if __name__ == "__main__":

    main()

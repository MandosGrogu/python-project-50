from argparse import ArgumentParser
from json import load as json_load

from yaml import CLoader
from yaml import load as yml_load

from gendiff.scripts.file_parse import parse
from gendiff.scripts.format.format import format_diff

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


def generate_diff(f1, f2, format_name='stylish'):

    file1 = read_file_acc_to_format(f1)
    file2 = read_file_acc_to_format(f2)

    diff = parse(file1, file2)

    return format_diff(diff, format_name)


def main():

    parser = ArgumentParser(
        prog='gendiff', 
        usage='%(prog)s [-h] [-f FORMAT] first_file second_file', 
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', nargs='+')
    parser.add_argument('second_file', nargs='+')
    parser.add_argument('-f', '--format', 
        default='stylish', 
        nargs='?', 
        help='set format of output')

    args = parser.parse_args()

    if args.first_file and args.second_file:
        return generate_diff(args.first_file[0], 
            args.second_file[0], 
            format_name=args.format)


if __name__ == "__main__":

    main()

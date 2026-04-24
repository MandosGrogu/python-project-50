from argparse import ArgumentParser

from gendiff.generate_diff import Generator


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
        gen = Generator()
        f1 = args.first_file[0]
        f2 = args.second_file[0]
        return gen.generate_diff(f1, f2, format_name=args.format)


if __name__ == "__main__":

    main()

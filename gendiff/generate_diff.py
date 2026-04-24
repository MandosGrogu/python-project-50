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


class Generator:

    def __init__(self, format_name=None):

        if format_name:
            self.format_name = format_name
        else:
            self.format_name = 'stylish'
    
    def read_file_acc_to_format(self, f):

        self.f = f

        self.file_format = self.f.split('.')[-1]
        if self.file_format.lower() in APPROPRIATE_FILE_FORMATS.keys():
            self.file_format = APPROPRIATE_FILE_FORMATS[self.file_format]

        if self.file_format == 'json':
            self.file = json_load(open(self.f))
        elif self.file_format == 'yml':
            self.file = yml_load(open(self.f), Loader=CLoader)

        return self.file

    def generate_diff(self, f1, f2, format_name='stylish'):

        self.format_name = format_name
        self.f1 = f1
        self.f2 = f2
        self.file1 = self.read_file_acc_to_format(self.f1)
        self.file2 = self.read_file_acc_to_format(self.f2)

        self.diff = parse(self.file1, self.file2)

        return format_diff(self.diff, self.format_name)
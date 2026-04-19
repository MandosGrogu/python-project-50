import os
from gendiff.scripts.gendiff import generate_diff

def test_gendiff():

    base_path = os.getenv('GITHUB_WORKSPACE', os.getcwd())
    file1_path = os.path.join(base_path, 'test_data/f1.json')
    file2_path = os.path.join(base_path, 'test_data/f2.json')

    assert generate_diff(file1_path, file2_path) == '''- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True
'''

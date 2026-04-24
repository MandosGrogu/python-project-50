import json
import os

from gendiff.generate_diff import Generator


def test_gendiff():
    
    gen = Generator()

    f1_p = os.path.join(os.getcwd(), 'tests/test_data/f1.json')
    f2_p = os.path.join(os.getcwd(), 'tests/test_data/f2.json')
    tru_p = os.path.join(os.getcwd(), 'tests/test_data/f2_gr_tru.txt')

    with open(tru_p, 'r', encoding='utf-8') as f:
        tru = f.read()
        
    assert gen.generate_diff(f1_p, f2_p) == tru

    f1_json_p = os.path.join(os.getcwd(), 'tests/test_data/filepath1.json')
    f2_json_p = os.path.join(os.getcwd(), 'tests/test_data/filepath2.json')
    tru_p1 = os.path.join(os.getcwd(), 'tests/test_data/fpath2_gr_tru.txt')

    with open(tru_p1, 'r', encoding='utf-8') as f:
        tru1 = f.read()
    
    assert gen.generate_diff(f1_json_p, f2_json_p, format_name='stylish') == tru1

    tru_p0 = os.path.join(os.getcwd(), 'tests/test_data/fpath2_gr_tru.json')

    tru0 = json.dumps(json.load(open(tru_p0)), indent=4)
    
    assert gen.generate_diff(f1_json_p, f2_json_p, format_name='json') == tru0

    f1_yml_p = os.path.join(os.getcwd(), 'tests/test_data/filepath1.yaml')
    f2_yml_p = os.path.join(os.getcwd(), 'tests/test_data/filepath2.yaml')
    tru_p2 = os.path.join(os.getcwd(), 'tests/test_data/fpath2_yml_gr_tru.txt')

    with open(tru_p2, 'r', encoding='utf-8') as f:
        tru2 = f.read()

    assert gen.generate_diff(f1_yml_p, f2_yml_p, format_name='plain') == tru2
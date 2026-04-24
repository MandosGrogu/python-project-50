import os
import json
from gendiff.scripts.gendiff import generate_diff

def test_gendiff():

    base_path = os.getenv('GITHUB_WORKSPACE', os.getcwd())
    file1_path = os.path.join(os.getcwd(), 'tests/test_data/f1.json')
    file2_path = os.path.join(os.getcwd(), 'tests/test_data/f2.json')
    ground_truth_path = os.path.join(os.getcwd(), 'tests/test_data/f2_ground_truth.txt')

    with open(ground_truth_path, 'r', encoding='utf-8') as f:
        ground_truth = f.read()

    assert generate_diff(file1_path, file2_path) == ground_truth

    file1_nested_json_path = os.path.join(os.getcwd(), 'tests/test_data/filepath1.json')
    file2_nested_json_path = os.path.join(os.getcwd(), 'tests/test_data/filepath2.json')
    ground_truth_path1 = os.path.join(os.getcwd(), 'tests/test_data/filepath2_ground_truth.txt')

    with open(ground_truth_path1, 'r', encoding='utf-8') as f:
        ground_truth1 = f.read()

    assert generate_diff(file1_nested_json_path, file2_nested_json_path, format_name='stylish') == ground_truth1

    ground_truth_path0 = os.path.join(os.getcwd(), 'tests/test_data/filepath2_ground_truth.json')

    ground_truth0 = json_load(open(f))

    assert generate_diff(file1_nested_json_path, file2_nested_json_path, format_name='json') == ground_truth0

    file1_nested_yaml_path = os.path.join(os.getcwd(), 'tests/test_data/filepath1.yml')
    file2_nested_yaml_path = os.path.join(os.getcwd(), 'tests/test_data/filepath2.yml')
    ground_truth_path2 = os.path.join(os.getcwd(), 'tests/test_data/filepath2_yml_ground_truth.txt')

    with open(ground_truth_path2, 'r', encoding='utf-8') as f:
        ground_truth2 = f.read()

    assert generate_diff(file1_nested_yaml_path, file2_nested_yaml_path, format_name='plain') == ground_truth2
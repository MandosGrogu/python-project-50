import os
import re

DIFF_TYPE_CONVERT ={
    'minus': 'was removed',
    'plus': 'was added with value:',
    '_': 'was updated'
}

def add_full_paths(diff, parent=None):

    result = diff
    for line in result:
        if isinstance(line['value'], list):
            if line['lvl'] == 1 or parent is None:
                parent = line['key']
                add_full_paths(line['value'], parent)
                continue
            elif line['lvl'] < 3:
                parent = parent.split('.')[0]
                parent += f'.{line['key']}'
            else:
                if len(parent.split('.')) > line['lvl']:
                    parent = '.'.join(parent.split('.')[0:line['lvl']-2])
                parent += f'.{line['key']}'
            line['key'] = parent
            add_full_paths(line['value'], parent)
        else:
            if parent is not None:
                if len(parent.split('.')) >= line['lvl']:
                    parent = '.'.join(parent.split('.')[0:line['lvl']-1])
                line['key'] = parent + '.' + line['key']

    return result

def plain_formatter(diff):

    diff_with_full_paths = add_full_paths(diff)
    
    def inner(diff_with_full_paths):

        result_str = ''

        check_i = -1

        for i, element in enumerate(diff_with_full_paths):
            if check_i != -1:
                check_i = -1
                continue
            element_val = element['value']
            if isinstance(element_val, list) and element['diff_type'] == 'common':
                result_str += inner(element_val)
            else:
                if isinstance(element_val, list):
                    res_val = '[complex value]'
                elif isinstance(element_val, str):
                    res_val = "'" + element_val + "'"
                else:
                    res_val = str(element_val)
                doubl_key = [n for n, line in enumerate(diff_with_full_paths) if n !=i and line['key'] == element['key']]
                if len(doubl_key) > 0:
                    if isinstance(diff_with_full_paths[doubl_key[0]]['value'], list):
                        res_val1 = '[complex value]'
                    elif isinstance(diff_with_full_paths[doubl_key[0]]['value'], str):
                        res_val1 = "'" + diff_with_full_paths[doubl_key[0]]['value'] + "'"
                    else:
                        res_val1 = str(diff_with_full_paths[doubl_key[0]]['value'])

                    result_str += f'Property "{element['key']}" {DIFF_TYPE_CONVERT['_']}. From {res_val} to {res_val1}{os.linesep}'
                    check_i = i
                elif element['diff_type'] == 'minus':
                    result_str += f'Property "{element['key']}" {DIFF_TYPE_CONVERT[element['diff_type']]}{os.linesep}'
                elif element['diff_type'] == 'plus':
                    result_str += f'Property "{element['key']}" {DIFF_TYPE_CONVERT[element['diff_type']]} {res_val}{os.linesep}'
                
                
        return result_str
    return inner(diff_with_full_paths)
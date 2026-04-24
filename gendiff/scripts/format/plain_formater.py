import os

DIFF_TYPE_CONVERT = {
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
                    parent = '.'.join(parent.split('.')[0:line['lvl'] - 2])
                parent += f'.{line['key']}'
            line['key'] = parent
            add_full_paths(line['value'], parent)
        else:
            if parent is not None:
                if len(parent.split('.')) >= line['lvl']:
                    parent = '.'.join(parent.split('.')[0:line['lvl'] - 1])
                line['key'] = parent + '.' + line['key']

    return result


def plain_formatter(diff):

    dfp = add_full_paths(diff)
    
    def inner(dfp):

        result_str = ''
        check_i = -1

        for i, el in enumerate(dfp):
            if check_i != -1:
                check_i = -1
                continue
            el_val = el['value']
            if isinstance(el_val, list) and el['diff_type'] == 'common':
                result_str += inner(el_val)
            else:
                if isinstance(el_val, list):
                    res_val = '[complex value]'
                elif isinstance(el_val, str):
                    res_val = "'" + el_val + "'"
                else:
                    res_val = str(el_val)
                d_k = [n for n, ln in enumerate(dfp) if n != i and ln['key'] == el['key']]

                if len(d_k) > 0:
                    res_val1 = format_val(el_val)
                    result_str += f'Property "{el['key']}" \
                    {DIFF_TYPE_CONVERT['_']}\
                    . From {res_val} to {res_val1}{os.linesep}'
                    check_i = i
                elif el['diff_type'] == 'minus':
                    result_str += f'Property "{el['key']}" \
                    {DIFF_TYPE_CONVERT[el['diff_type']]}{os.linesep}'
                elif el['diff_type'] == 'plus':
                    result_str += f'Property "{el['key']}" \
                    {DIFF_TYPE_CONVERT[el['diff_type']]} {res_val}{os.linesep}'

        return result_str

    return inner(dfp)


def format_val(val):
    if isinstance(val, list):
        new_val = '[complex value]'
    elif isinstance(val, str):
        new_val = "'" + val + "'"
    else:
        new_val = str(val)
    return new_val
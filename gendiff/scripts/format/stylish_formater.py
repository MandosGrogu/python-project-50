import os
from json import dumps as js_dumps

IND = 4

D_TP = {
    'minus': '-',
    'plus': '+',
    'common': ' '
}


def stylish_formatter(diff):

    res_str = ''
    n = os.linesep

    for el in diff:
        el_v = el['value']
        if isinstance(el_v, list):
            res_str += f'{" " * ((el['lvl'] * IND) - 2)}'
            res_str += f'{D_TP[el['df_tp']]} {el['key']}: {"{"}{n}'
            res_str += f'{stylish_formatter(el_v)}{n}'
            res_str += f'{" " * ((el['lvl'] * IND))}{"}"}{n}'
        else:
            js_val = format_val(el_v)
            res_str += f'{" " * ((el['lvl'] * IND) - 2)}{D_TP[el['df_tp']]}'
            res_str += f' {el['key']}: {js_val}{n}'

    return res_str.replace("\n\n", "\n")


def format_val(val):

    if not isinstance(val, str):
        new_val = js_dumps(val)
    else:
        new_val = val
    return new_val
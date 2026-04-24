import os

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
            res_str += f'{" " * ((el['lvl'] * IND) - 2)}\
            {D_TP[el['diff_type']]} {el['key']}: {"{"}{n}'
            res_str += f'{stylish_formatter(el_v)}{n}\
            {" " * ((el['lvl'] * IND))}{"}"}{n}'
        else:

            res_str += f'{" " * ((el['lvl'] * IND) - 2)}\
            {D_TP[el['diff_type']]} {el['key']}: {el_v}{n}'

    return res_str.replace("\n\n", "\n")
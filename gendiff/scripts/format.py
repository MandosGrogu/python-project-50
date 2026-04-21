import os

INDENT = 4

DIFF_TYPE_CONVERT ={
    'minus': '-',
    'plus': '+',
    'common': ' '
}

def format_diff(diff, format_name):

    if format_name == 'stylish':
        formatted_str = stylish_formatter(diff)

    return formatted_str

def stylish_formatter(diff):

    result_str = ''

    for element in diff:
        element_val = element['value']
        if isinstance(element_val, list):
            result_str += f'{" " * ((element['lvl']*INDENT)-2)}{DIFF_TYPE_CONVERT[element['diff_type']]} {element['key']}: {"{"}{os.linesep}'
            result_str += f'{stylish_formatter(element_val)}{os.linesep}{" " * ((element['lvl']*INDENT))}{"}"}{os.linesep}'
        else:
            result_str += f'{" " * ((element['lvl']*INDENT)-2)}{DIFF_TYPE_CONVERT[element['diff_type']]} {element['key']}: {element_val}{os.linesep}'

    return result_str.replace("\n\n", "\n")
import os
import re
import json

from gendiff.scripts.format.plain_formater import add_full_paths

def json_formatter(diff):

    diff_with_full_paths = add_full_paths(diff)

    def inner(diff):

        result = {}

        for i, element in enumerate(diff):
            element_val = element['value']
            if isinstance(element_val, list):
                if element['diff_type'] not in result.keys():
                    result[element['diff_type']] = {element['key']: '[complex value]'}
                else: 
                    result[element['diff_type']] = result[element['diff_type']] | {element['key']: '[complex value]'}
                for key in inner(element_val).keys():
                    if key in result.keys():
                        result[key] = result[key] | inner(element_val)[key]
                    else:
                        result[key] = inner(element_val)[key]
            else:
                if element['diff_type'] in result.keys():
                    result[element['diff_type']] = result[element['diff_type']] | {element['key']: element_val}
                else:
                    result[element['diff_type']] = {element['key']: element_val}
        return result

    return json.dumps(inner(diff_with_full_paths), indent=4)
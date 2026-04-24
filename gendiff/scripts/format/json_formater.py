import json

from gendiff.scripts.format.plain_formater import add_full_paths


def json_formatter(diff):

    diff_with_full_paths = add_full_paths(diff)

    def inner(diff):

        res = {}
        cv = '[complex value]'

        for i, el in enumerate(diff):
            el_val = el['value']
            if isinstance(el_val, list):
                if el['diff_type'] not in res.keys():
                    res[el['diff_type']] = {el['key']: cv}
                else: 
                    res[el['diff_type']] = res[el['diff_type']] | {el['key']: cv}
                for key in inner(el_val).keys():
                    if key in res.keys():
                        res[key] = res[key] | inner(el_val)[key]
                    else:
                        res[key] = inner(el_val)[key]
            else:
                if el['diff_type'] in res.keys():
                    res[el['diff_type']] = res[el['diff_type']] | {el['key']: el_val}
                else:
                    res[el['diff_type']] = {el['key']: el_val}
        return res

    return json.dumps(inner(diff_with_full_paths), indent=4)

def get_diff_type(dict1, dict2, lvl=0):

    common_k = dict1.keys() & dict2.keys()
    plus_k = dict2.keys() - dict1.keys()
    minus_k = dict1.keys() - dict2.keys()

    return common_k, plus_k, minus_k

def make_diff_dict(k, diftype, lvl, f1=None, f2=None):

    if f1 is None:
        if isinstance(f2[k], dict):
            result_dict= {'key': k, 'value': parse(f2[k], f2[k], lvl+1), 'diff_type': diftype, 'lvl': lvl}
        else:
            result_dict = {'key': k, 'value': f2[k], 'diff_type': diftype, 'lvl': lvl}
    elif f2 is None:
        if isinstance(f1[k], dict):
            result_dict= {'key': k, 'value': parse(f1[k], f1[k], lvl+1), 'diff_type': diftype, 'lvl': lvl}
        else:
            result_dict = {'key': k, 'value': f1[k], 'diff_type': diftype, 'lvl': lvl}
    else:
        if isinstance(f1[k], dict) and isinstance(f2[k], dict):
            result_dict= {'key': k, 'value': parse(f1[k], f2[k], lvl+1), 'diff_type': diftype, 'lvl': lvl}
        else:
            if f1[k] == f2[k]:
                if isinstance(f1[k], dict):
                    result_dict = {'key': k, 'value': parse(f1[k], f2[k], lvl+1), 'diff_type': diftype, 'lvl': lvl}
                else:
                    result_dict = {'key': k, 'value': f1[k], 'diff_type': diftype, 'lvl': lvl}
            else:
                if isinstance(f1[k], dict):
                    result_dict = result_dict = {
                        'minus': {'key': k, 'value': parse(f1[k], f1[k], lvl+1), 'diff_type': 'minus', 'lvl': lvl}, 
                        'plus': {'key': k, 'value': f2[k], 'diff_type': 'plus', 'lvl': lvl}
                    }
                elif isinstance(f2[k], dict):
                    result_dict = result_dict = {
                        'minus': {'key': k, 'value': f1[k], 'diff_type': 'minus', 'lvl': lvl}, 
                        'plus': {'key': k, 'value': parse(f2[k], f2[k], lvl+1), 'diff_type': 'plus', 'lvl': lvl}
                    }
                else:
                    result_dict = {
                        'minus': {'key': k, 'value': f1[k], 'diff_type': 'minus', 'lvl': lvl}, 
                        'plus': {'key': k, 'value': f2[k], 'diff_type': 'plus', 'lvl': lvl}
                    }

    return result_dict

def parse(f1, f2, lvl=1):

    if isinstance(f1, dict) and isinstance(f2, dict):
        all_keys_list = sorted(list(dict.fromkeys(list(f1.keys()) + list(f2.keys()))))

        common, plus, minus = get_diff_type(f1, f2)
        
        intermediate_result = []

        for k in all_keys_list:
            if k in minus:
                intermediate_result.append(make_diff_dict(k, 'minus', lvl, f1=f1))
            if k in plus:
                intermediate_result.append(make_diff_dict(k, 'plus', lvl, f2=f2))
            if k in common:
                if len(list(make_diff_dict(k, 'common', lvl, f1=f1, f2=f2).keys())) > 2:
                    intermediate_result.append(make_diff_dict(k, 'common', lvl, f1=f1, f2=f2))
                else:
                    for val in make_diff_dict(k, 'common', lvl, f1=f1, f2=f2).values():
                        intermediate_result.append(val)
    else:
        return

    return intermediate_result
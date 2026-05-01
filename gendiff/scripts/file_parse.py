
def get_df_tp(dict1, dict2, lvl=0):

    common_k = dict1.keys() & dict2.keys()
    plus_k = dict2.keys() - dict1.keys()
    minus_k = dict1.keys() - dict2.keys()

    return common_k, plus_k, minus_k


def mk_df(k, diftype, lvl, f1=None, f2=None):

    if f1 is None:
        if isinstance(f2[k], dict):
            result_dict = {
                'key': k, 
                'value': parse(f2[k], f2[k], lvl + 1), 
                'df_tp': diftype, 
                'lvl': lvl}
        else:
            result_dict = {'key': k, 
            'value': f2[k], 
            'df_tp': diftype, 
            'lvl': lvl}
    elif f2 is None:
        if isinstance(f1[k], dict):
            result_dict = {'key': k, 
            'value': parse(f1[k], f1[k], lvl + 1), 
            'df_tp': diftype, 
            'lvl': lvl}
        else:
            result_dict = {'key': k, 
            'value': f1[k], 
            'df_tp': diftype, 
            'lvl': lvl}
    else:
        if isinstance(f1[k], dict) and isinstance(f2[k], dict):
            result_dict = {'key': k, 
            'value': parse(f1[k], f2[k], lvl + 1), 
            'df_tp': diftype, 
            'lvl': lvl}
        else:
            if f1[k] == f2[k]:
                if isinstance(f1[k], dict):
                    result_dict = {'key': k, 
                    'value': parse(f1[k], f2[k], lvl + 1), 
                    'df_tp': diftype, 
                    'lvl': lvl}
                else:
                    result_dict = {'key': k, 
                    'value': f1[k], 
                    'df_tp': diftype, 
                    'lvl': lvl}
            else:
                if isinstance(f1[k], dict):
                    result_dict = result_dict = {
                        'minus': {'key': k, 
                        'value': parse(f1[k], f1[k], lvl + 1), 
                        'df_tp': 'minus', 
                        'lvl': lvl}, 
                        'plus': {'key': k, 
                        'value': f2[k], 
                        'df_tp': 'plus', 
                        'lvl': lvl}
                    }
                elif isinstance(f2[k], dict):
                    result_dict = result_dict = {
                        'minus': {'key': k, 
                        'value': f1[k], 
                        'df_tp': 'minus', 
                        'lvl': lvl}, 
                        'plus': {'key': k, 
                        'value': parse(f2[k], f2[k], lvl + 1), 
                        'df_tp': 'plus', 
                        'lvl': lvl}
                    }
                else:
                    result_dict = {
                        'minus': {'key': k, 
                        'value': f1[k], 
                        'df_tp': 'minus', 
                        'lvl': lvl}, 
                        'plus': {'key': k, 
                        'value': f2[k], 
                        'df_tp': 'plus', 
                        'lvl': lvl}
                    }

    return result_dict


def parse(f1, f2, lvl=1):

    if isinstance(f1, dict) and isinstance(f2, dict):
        all_k_l = sorted(list(dict.fromkeys(list(f1.keys()) + list(f2.keys()))))

        common, plus, minus = get_df_tp(f1, f2)
        
        inter_res = []

        for k in all_k_l:
            if k in minus:
                inter_res.append(mk_df(k, 'minus', lvl, f1=f1))
            if k in plus:
                inter_res.append(mk_df(k, 'plus', lvl, f2=f2))
            if k in common:
                if len(list(mk_df(k, 'common', lvl, f1=f1, f2=f2).keys())) > 2:
                    inter_res.append(mk_df(k, 'common', lvl, f1=f1, f2=f2))
                else:
                    for val in mk_df(k, 'common', lvl, f1=f1, f2=f2).values():
                        inter_res.append(val)
    else:
        return

    return inter_res
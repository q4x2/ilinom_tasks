def is_templ_match(tmpl_dict):
    print(tmpl_dict)
    for char in tmpl_dict:
        if tmpl_dict[char]['cnt'] != tmpl_dict[char]['m_cnt']:
            return False
    return True


def calc_templ_match(str, tmpl):
    tmpl_dict = {}
    for char in tmpl:
        if char not in tmpl_dict:
            tmpl_dict[char] = {'epoch':0, 'cnt':1, 'm_cnt': 0}
        else:
            tmpl_dict[char]['cnt'] += 1
    epoch = 0
    for char in str:
        if char in tmpl_dict:
            if epoch == tmpl_dict[char]['epoch']:
                tmpl_dict[char]['m_cnt'] += 1
                if tmpl_dict[char]['m_cnt'] > tmpl_dict[char]['cnt']:
                    epoch += 1
                    tmpl_dict[char]['m_cnt'] = 1
            else:
                tmpl_dict[char]['m_cnt'] = 1
                tmpl_dict[char]['epoch'] = epoch
        else:
            epoch += 1
    return is_templ_match(tmpl_dict)

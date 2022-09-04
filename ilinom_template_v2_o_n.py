def calc_templ_match(str, tmpl):
    tmpl_dict = {}
    for char in tmpl:
        if char not in tmpl_dict:
            tmpl_dict[char] = {'epoch':0, 'cnt':1, 'm_cnt': 0}
        else:
            tmpl_dict[char]['cnt'] += 1
    epoch = 0
    tmpl_sz = len(tmpl)
    gl_cnt = 0
    for char in str:
        if char in tmpl_dict:
            if epoch == tmpl_dict[char]['epoch']:
                tmpl_dict[char]['m_cnt'] += 1
                if tmpl_dict[char]['m_cnt'] > tmpl_dict[char]['cnt']:
                    epoch += 1
                    gl_cnt = 1
                    tmpl_dict[char]['m_cnt'] = 1
                    tmpl_dict[char]['epoch'] = epoch
                else:
                    gl_cnt += 1
                    if gl_cnt == tmpl_sz:
                        return True
            else:
                tmpl_dict[char]['m_cnt'] = 1
                tmpl_dict[char]['epoch'] = epoch
                gl_cnt += 1
                if gl_cnt == tmpl_sz:
                    return True
        else:
            epoch += 1
            gl_cnt = 0
    return False

def is_template_match(input_str, templ_str):
    len_input = len(input_str)
    len_templ = len(templ_str)
    if len_input < len_templ or len_templ == 0: 
        return False
    list_templ = list(templ_str)
    cnt = 0
    for chr in input_str:
        if chr in list_templ:
            list_templ.remove(chr)
            cnt += 1
            if cnt == len_templ:
                return True
        else:
            list_templ = list(templ_str)
            cnt = 0
    return False

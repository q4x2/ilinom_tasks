def range_gen(num_list):
    prev_num = None
    num_range = ''
    num_count = len(num_list) - 1
    curr_elem_num = 0
    for num in num_list:
        if curr_elem_num == num_count and num - prev_num == 1:    
            yield num_range + '-' + str(num)
            return
        if curr_elem_num == num_count and num - prev_num > 1:
            yield num_range + '-' + str(prev_num)
            yield str(num)
            return
        if prev_num: 
            if num - prev_num > 1:
                num_range += '-' + str(prev_num)
                prev_num = num
                yield num_range
                num_range = str(num)
            else:
                prev_num = num
        else:
            num_range += str(num)
            prev_num = num
        curr_elem_num += 1

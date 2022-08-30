def find_key_index(array_shifted, key) -> int:
    low_pointer = 0
    high_pointer = len(array_shifted) - 1
    
    
    def find_pivot(array_shifted, low_pointer, high_pointer) -> int:
        
        if high_pointer < low_pointer:
            return -1
        if high_pointer == low_pointer:
            return low_pointer

        mid = int((low_pointer + high_pointer)/2)
        
        if array_shifted[mid] > array_shifted[mid+1] and mid < high_pointer:
            return mid
        if array_shifted[mid] < array_shifted[mid-1] and mid > low_pointer:
            return (mid-1)
        if array_shifted[low_pointer] >= array_shifted[mid]:
            return find_pivot(array_shifted, low_pointer, mid-1)
        return find_pivot(array_shifted, mid+1, high_pointer)

    
    def find_key_binary(array_shifted, low_pointer, high_pointer, key) -> int:
        
        if high_pointer < low_pointer:
            return -1

        mid = int((low_pointer + high_pointer)/2)
        if key == array_shifted[mid]:  
            return mid
        if key > array_shifted[mid]:
            return find_key_binary(array_shifted, mid+1, high_pointer, key)
        return find_key_binary(array_shifted, low_pointer, mid-1, key)
    
    pivot = find_pivot(array_shifted, low_pointer, high_pointer)
    if pivot == -1:
        return find_key_binary(array_shifted, 0, high_pointer, key)

    if key == array_shifted[pivot]:  
        return pivot

    if key > array_shifted[0]:
        return find_key_binary(array_shifted, low_pointer, pivot-1, key)
    else: 
        return find_key_binary(array_shifted, pivot+1, high_pointer, key)

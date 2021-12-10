# sequential searches
def sequential_max(the_list):
    current_index = 0
    max_val = the_list[0] # set the max_value as the first item

    while current_index < len(the_list) - 1: # go through the rest of the list
        current_index += 1
        if the_list[current_index] > max_val: # if it finds a larger value
            max_val = the_list[current_index] # set our new max value
        
    return max_val

def sequential_min(the_list):
    current_index = 0
    min_val = the_list[0] # set the min_value as the first item

    while current_index < len(the_list) - 1: # go through the rest of the list
        current_index += 1
        if the_list[current_index] < min_val: # if it finds a smaller value
            min_val = the_list[current_index] # set our new min value
        
    return min_val


def sequential_equal(search_val, the_list):
    current_index = 0
    found = False
    
    while current_index < len(the_list) and found == False:
        
        if the_list[current_index] == search_val:
            found = True
        
        current_index += 1

    return found


# binary search
def binary_search(search_val, the_list):
    left_index = 0
    right_index = len(the_list) - 1
    found = False

    while left_index <= right_index and found != True:
        mid_index = (left_index + right_index) // 2  # average and floor
        if the_list[mid_index] == search_val:        # is the mid val the search val
            found = True
        elif the_list[mid_index] > search_val:
            right_index = mid_index - 1
        elif the_list[mid_index] < search_val:
            left_index = mid_index + 1

    if found:
        return mid_index
    else:
        return None
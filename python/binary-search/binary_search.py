def find(search_list, value):

    if len (search_list) == 0:
        raise ValueError("value not in array")

    low = search_list[0]
    high = search_list[-1]
    while low <= high:
        mid = (search_list.index(low) + search_list.index(high)) // 2
        if search_list[mid] == value:
            return mid
        elif low == high:
            break
        elif search_list[mid] < value:
            low = search_list[mid+1]
        elif search_list[mid] > value:
            high = search_list[mid]

    raise ValueError("value not in array")





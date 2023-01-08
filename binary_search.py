lst = [4,2,1,10,5,3,100]
search_item = 3

def binary_search(lst, value):
    #base case here
    if len(lst) == 1:
        return lst[0] == value

    mid = len(lst)/2
    if lst[mid] < value:
        return binary_search(lst[:mid], value)
    elif lst[mid] > value:
        return binary_search(lst[mid+1:], value)
    else:
        return True


binary_search(lst,search_item)


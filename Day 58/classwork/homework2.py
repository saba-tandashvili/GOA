def remove_largest(lst, value):
    if not lst:
        return []
    largest = max(lst)
    lst.remove(largest)
    if largest == value:
        return lst
    return remove_largest(lst, value)
lst = [1, 2, 3, 4, 5]
value = 4

updated_lst = remove_largest(lst, value)

print(updated_lst)
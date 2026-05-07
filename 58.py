def filter_list(lst, son):
    new_lst = lst.copy()
    if son == 0:
        for num in new_lst:
            if num % 2 == 0:
                lst.remove(num)
        return lst
    else:
        for num in new_lst:
            if num % 2 == 1:
                lst.remove(num)
        return lst

print(filter_list([3, 5, 3, 6], 1))
# a = 1
# 1. number = 3; list = [5, 3, 6]
# 2
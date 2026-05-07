def filter_odd(sequence):
    return filter(lambda x : x % 2 == 0, sequence)

print(list(filter_odd([1, 2, 4, 6, 7])))
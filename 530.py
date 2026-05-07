# map(func, iterable)
def map(func, seqeunce):
    new_lst =[]
    for n in seqeunce:
        new_lst.append(func(n))

    return new_lst

print(map(lambda x: x + 2, [-5, 0, 5]))
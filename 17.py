for son in range(1000, 10000):
    # Raqamlarni ajratish
    ming = son // 1000
    yuz = (son // 100) % 10
    on = (son // 10) % 10
    bir = son % 10
    
    yigindi = ming + yuz + on + bir
    
    # Shart: yig‘indi juft bo‘lsa
    if yigindi % 2 == 0:
        print(son, end=" ")



def sum_of_digits(number):
    s = 0
    for char in str(number):
        digit = int(char)
        s += digit

for son in range(1000, 10000):
    if sum_of_digits(son) % 2 == 0:
        print(son, end=" ")
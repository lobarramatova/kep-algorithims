# stringni teskarisiga o'girish
text = "abcd"
print(text[1 : 3])
print(text[0 : 4])
print(text[0:: ])
print(text[::-1])

def reverse_number(num):
    return int(str(num)[::-1])
print(reverse_number(1589))
for number in range(1000, 10000):
    if reverse_number(number) == 4 * number:
        print(number)
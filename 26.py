n = int(input())
s = 0
for son in range(1, n + 1):
    if (son % 12 == 0) or (son % 5 == 0):
        s += 1
print(s)

n = int(input())
print(n // 12 + n // 5 - n // 60)
n = int(input())
s = 1
for son in range(1, n + 1):
    s*= son
print(s)

# n = 4
# siklldagi qadamlar:
# 1. n = 1 son = 1 s *= 1 * 1 = 1
# 2. n = 2 son = 1 s *= 1 * 2 = 2
# 3. n = 3 son = 2 s *= 2 * 3 = 6
# 4. n = 4 son = 6 s *= 6 * 4 = 24
# 1 + 2 + 3 + .... + (n - 1)
n = int(input())
s = 0
for son in range(1, n + 1):
    s += son

print(s)

import math
print(int(math.sqrt(8)))
print(int(math.sqrt(9)))


n = int(input())
y = 0

for i in range(1, n + 1):
    y += int(math.sqrt(i))

print(y)
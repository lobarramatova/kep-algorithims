n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] == min(a):
        print(i + 1, end=" ")
        break


n = int(input())
a = list(map(int, input().split()))
position = a.index(min(a)) + 1
print(position)
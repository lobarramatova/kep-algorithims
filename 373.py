n = int(input())
a = list(map(int, input().split()))
# print(max(a))
max_value = a[0]
for element in a:
    if element > max_value:
        max_value = element

print(max_value)


# n = int(input())
# a = list(map(int, input().split()))
# # print(max(a))
# min_value = a[0]
# for element in a:
#     if element < min_value:
#         min_value = element

# print(min_value)

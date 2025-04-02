lst = [10, 7, 3, 4, 6, 5, 2, 1, 9, 8]

for i in range(len(lst)):
    for j in range(len(lst) - 1):
        if lst[j] > lst[j + 1]:
            temp = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = temp

print(lst)

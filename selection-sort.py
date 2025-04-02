lst = [10, 7, 3, 4, 6, 5, 2, 1, 9, 8]
tmp = 0
for i in range(len(lst)):
     for j in range(len(lst)):
          if lst[i] < lst[j]:
               tmp = lst[i]
               lst[i] = lst[j]
               lst[j] = tmp
print(lst)
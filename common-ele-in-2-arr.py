arr1 = [1, 2, 3, 4, 6]
arr2 = [3, 4, 5, 6]

res = []

for i in arr1:
     if i in arr2:
          res.append(i)
print(res)
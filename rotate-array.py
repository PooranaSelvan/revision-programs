inp = [1, 2, 3, 4, 5, 6, 7]
n = 3
# op = [5, 6, 7, 1, 2, 3, 4]

arr = []

for i in range(1, n + 1):
     arr.append(inp[-i])
# print(arr)
arr.sort()

res = []

for j in arr:
     res.append(j)


for k in inp:
     if k not in res:
          res.append(k)
          
print(res)
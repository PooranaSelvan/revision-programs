arr = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
]

# print(len(arr))
res = 0


# for i in range(len(arr)):
#      res += arr[i][i]

for i in range(len(arr)):
     res += arr[i][len(str(i)) + 1]
     
print(res)
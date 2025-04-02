inp = [2, 4, 6, 8, 10, 14]
# Output: 12

for i in range(2, inp[-1] + 2, 2):
     if i not in inp:
          print(i)
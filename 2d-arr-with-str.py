s = "abcdefghij"

res = []
# print(len(s))
for i in range(len(s)):
     for j in range(1):
          if len(s) == i + 1:
               break
          else:
               res.append([s[i], s[i + 1]])
print(res)
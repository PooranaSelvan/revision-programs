s = "The quick brown fox"

# print(len(s.split(" ")))

res = []
st = ''


for i in s:
     if i == ' ':
          res.append(st)
          st = ''
          continue
     else:
          st += i
res.append(st)
print(len(res))
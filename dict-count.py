d = {}
s = "gggsshr"
st = ''
c = 0

for i in s:
     if i in st:
          d[i] += 1
     else:
          c += 1
          d[i] = c
     st += i
     c = 0
print(d)
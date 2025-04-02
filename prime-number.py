n = 10

res = []

for i in range(2, n):
     c = 0
     for j in range (2, i):
          if i % j == 0:
               c+=1
               break
     if c==0:
          res.append(i)
print(res)
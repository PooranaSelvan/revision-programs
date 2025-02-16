n = 5

for i in range(n):
     c = 0
     for j in range (2, n +1):
          if i%j == 0:
               c+=1
     if c==0:
          print(i)
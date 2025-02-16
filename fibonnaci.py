a, b = 0, 1
lst = []

for i in range(10):
     lst.append(a)
     a, b = b, a + b
print(lst)
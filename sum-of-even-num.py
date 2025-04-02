n = 10

even = []

for i in range(1, n + 1):
     if i % 2 == 0:
          even.append(i)

# print(sum(even))

res = 0

for i in even:
     res += i
print(res)
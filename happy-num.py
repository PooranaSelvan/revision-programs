inp = 23
# Output: True (because 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, and so on, leading to 1)

res = 0

while inp!= 1:
     res = 0
     while inp > 0:
          res += (inp % 10) ** 2
          inp //= 10
     inp = res
# print(res)

if res == 1:
     print(True)
else:
     print(False)
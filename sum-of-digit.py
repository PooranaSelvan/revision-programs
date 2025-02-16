def sumofdigit(n):
     num = n
     res = 0
     for i in range(len(str(n))):
          last = n % 10
          res += last
          n = n // 10
     print(res)

sumofdigit(2314)
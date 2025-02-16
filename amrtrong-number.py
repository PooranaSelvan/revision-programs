def amstrong(n):
     sum = 0
     num = n
     for i in range (len(str(n))):
          last = n % 10  #to get a last number
          sum += last ** len(str(num))
          n = n // 10 #to remove a last number
     if sum == num:
          print ("Armstrong")
     else:
          print("not")

amstrong(153)
inp = "hhhbbaaba"

lst = []


for i in inp:
     if i not in lst:
          lst.append(i)
          
     if i in lst:
          lst.append(i)
          lst.reverse()
          
print(lst)
          
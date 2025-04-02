s = "swiss"
# op = w  -- because w is unique
c = []
for i in s:
     c.append(str(s.count(i)))



for j in range(len(c)):
     if c[j] == "1":
          print(s[j])
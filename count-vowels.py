s = "hello"
vowels = 0
consonants = 0

v = "aeiou"

for i in s.lower():
     if i in v:
          vowels += 1
     else:
          consonants += 1
print(f"Vowels: {vowels}, Consonants: {consonants}")
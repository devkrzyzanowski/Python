text = input("Podaj tekst do szyfrowania : ")
result = ""
for i in text:
     v = ord(i) + 1
     result = result + chr(v)
print(result)

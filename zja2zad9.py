var = ""
for x in range(65, 91):
     var = var + chr(x)
     var = var + chr(x+32)
print(var)

var = ""
for x in range(65, 91):  
     var = var + chr(x+32)
     var = var + chr(x)
print(var)
    

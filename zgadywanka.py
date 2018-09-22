import random
max = 10
data = random.randint(1,max)

for i in range(6):
    print("Proba" , i+1)

    odp = input("Jaka liczbe od 1 do 10 wylosowano ")
    if data == int(odp):
        print("Hura!!!!")
        break
    elif i==5:
        print("wylosowano ", data)
    else:
        if data > int(odp):
            print("za niska!")
        elif data < int(odp):
            print("za wysoka!")

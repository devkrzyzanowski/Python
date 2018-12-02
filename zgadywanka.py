import random
min = int(input("Podaj minimalna liczbe : "))
max = int(input("Podaj maxymalna liczbe : "))


data = random.randint(min,max)



for i in range(6):
    print("Proba" , i+1)
    odp = input("Jaka liczbe od " + str(min) + " do " + str(max) + " wylosowano")
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

firstValue = input("Podaj liczbe poczatkowa : ")
secondValue = input("Podaj liczbe koncowa : ")
space = input("Podaj odstep : ")

score = int((int(secondValue) - int(firstValue)) / int(space))
print("Wynik : ", score)

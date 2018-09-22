
taxFee = 0.23
registerFee = 0.05
dealerFee = 2000
deliveryFee = 350

price = input("Podaj cenę podstawową samochodu :")

priceWithTax = float(price) * taxFee
priceWithRegisterFee = float(price) * registerFee
finalPrice = float(price) + priceWithTax + priceWithRegisterFee + dealerFee + deliveryFee

print()
print("---------------------------------------------")
print("               cena podstawowa : ", price)
print("              wysokosc podatku : ", priceWithTax)
print("wysokosc oplaty rejestracyjnej : ", priceWithRegisterFee)
print("                 opłata dilera : ", dealerFee)
print("                opłata dostawa : ", deliveryFee)
print("---------------------------------------------")
print("                   cena łączna : ", finalPrice)

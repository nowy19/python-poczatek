import wartosc_lokaty.lokata

kapital = float(input("Podaj wartość wpłaconego kapitału: "))
oprocentowanie = float(input("Podaj wartość oprocentowania: "))
czas = float(input("Podaj długość lokaty: "))

zysk = wartosc_lokaty.lokata.wartosc_lokaty(kapital, oprocentowanie, czas)

print(f"Zysk wyniesie {zysk:.2f}zł")

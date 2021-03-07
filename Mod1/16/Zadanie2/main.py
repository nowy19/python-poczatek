import triangle

a = float(input("Podaj długość pierwszej przyprostokątnej: "))
b = float(input("Podaj długość drugiej przyprostokątnej: "))

c = triangle.przeciwprostokatna(a, b)

print(f"Długość przeciwprostokątnej wynosi {c}")

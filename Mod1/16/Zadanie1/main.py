import avarage_speed

distance = float(input("Podaj dystans w km: "))
time = float(input("Podaj czas w h:"))

speed = avarage_speed.avarage_speed(distance, time)

print(f"Średnia prędkość wynosi {speed} km/h")

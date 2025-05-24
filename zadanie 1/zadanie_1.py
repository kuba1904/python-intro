
# zadanie_1.py


# Tworzenie dwóch list
names = ["Anna", "Bartek", "Celina"]
scores = [85, 90, 78]

# Łączenie list za pomocą zip()
# Dokumentacja: https://docs.python.org/3/library/functions.html#zip
combined = list(zip(names, scores))
print("Połączone dane:", combined)

# Wykorzystanie funkcji z modułu standardowego (random)
# Dokumentacja: https://docs.python.org/3/library/random.html
import random
random_score = random.randint(50, 100)
print("Losowo wygenerowany wynik:", random_score)

# Obsługa wyjątku try-except
# Dokumentacja: https://docs.python.org/3/library/exceptions.html#valueerror
try:
    user_input = int(input("Podaj liczbę całkowitą: "))
    print("Podałeś liczbę:", user_input)
except ValueError:
    print("Błąd: To nie była liczba całkowita!")


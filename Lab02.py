# Übungen:

# Das kleine EinmalEins:
# Erstelle eine Schleife, die das einmaleins von 1 bis 10 berechnet und jeden einzelnen Schritt in der Konsole
# wiedergibt

# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ...
# 10 x 10 = 100

# Tipp: Verschachtelte Schleife, die Range funktion und die f-Strings für die Ausgabe

# FizzBuzz:
# EIne Schleife die von 1 bis 100(inklusive) hochzählt
# SOll jede der Zahlen auf ihre Teilbarkeit prüfen
# Falls die Zahl durch 3 Teilbar ist soll in der Konsole Fizz ausgegeben werden
# Falls die Zahl durch 5 Teilbar ist soll in der Konsole Buzz ausgegeben werden
# Falls  die Zahl sowohl durch 3 als auch 5 teilbar ist soll FizzBuzz in der Konsoel stehen
# Falls sie durch keine der beiden Zahlen teilbar ist soll die Zahl selber ausgegeben werden

# 3 => Fizz
# 5 => Buzz
# 4 => 4
# 15 => FIzzBuzz

# for i in range(1, 101, 1):
#     if i % 5 == 0 and i % 3 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)

for i in range(1, 101, 1):
    answer = ""
    if i % 3 == 0:
        answer += "Fizz"
    if i % 5 == 0:
        answer += "Buzz"
    if answer == "":
        print(i)
    else:
        print(answer)


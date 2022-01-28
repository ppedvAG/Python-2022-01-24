# Fehlerbehandlung
from personen import Mensch

namee = "Marius Sommer"

print(f"Hallo {namee}")
# Identation Erro / Tab Error => falsch eingerückt
# Name Error falscher Name für Funktion/Variable
# Errors führen immer zu Crash

# Exceptions
# Werden erhoben wenn syntaktisch richtiger Code nicht ausgeführt werden kann
# print(f"{namee - 2}")
# Exceptions können behandelt werden
# Der Traceback liest sich gleich wie bei syntax Fehlern

# Try.. und except block

# while True:
#     try:  # Try Block wird als erstes ausgeführt
#         # Und falls alles im Try ohne Fehler funktioniert, wird das Programm ganz normal ausgeführt
#         x = int(input("Gib mir eine Zahl: "))
#         y = int(input("Gib mir eine zweite Zahl: "))
#         try:
#             print(f"{x / y}")
#         except ZeroDivisionError as e:
#             print("Durch null kann nicht geteilt werden")
#             print(e)
#         break
#     except ValueError as e:  # Wenn es aber einen Fehler wirft, dann wird der except Block greifen
#         # Und der Fehler wird wie von uns programmiert behandelt
#         print("Das ist keine Zahl")
#         print(e)
#     except ZeroDivisionError as e:
#         print("Durch null kann nicht geteilt werden")
#         print(e)
#     except KeyboardInterrupt as e:
#         print(e)
#
# while True:
#     try:
#         x = int(input("Gib mir eine Zahl: "))
#         y = int(input("Gib mir eine zweite Zahl: "))
#         print(f"{x / y}")
#     except Exception as e:
#         print(e)


def recursive():
    print("führe aus")
    recursive()


# while True:
#     try:
#         recursive()
#     except RecursionError as e:
#         print(e)
#         # recursive()


class NoCoffe(Exception):
    def __init__(self):
        super().__init__("Ohne Kaffee geht nichts")


coffe= 3

try:
    if coffe < 2:
        raise NoCoffe # Erhebt den spezifizierten Fehler, kann mit except behandelt werden
except NoCoffe as e:
    print("Bitte gib deinen Entwicklern Kaffee")
    print(e)
except TypeError as e:  # Wird nur ausgeführt wenn der erwartete Fehler eintritt
    print(e)
except Exception as e:  # Wird ausgeführt wenn keine der vorherigen Except Blöcke eintrat
    print(e)
else:  # Wird nur ausgeführt wenn das Try erfolgreich war
    print("Ohne Fehler durchgeführt")
finally: # Wird immer ausgeführt
    print("Programm wird beendet")
    recursive()



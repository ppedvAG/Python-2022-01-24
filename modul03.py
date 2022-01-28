import os # Importiert das gesamte modul, muss aber jedesmal das präfix benutzen
import sys as s # Erlaubt mir das Modul sys mit dem Kürzel s aufzurufen
# from os import mkdir # Importiert nur mkdir

# In & Output
zahl1 = 150
zahl2 = 0.0000000012
text = "ü"
list = [1,2,3]
print(f"{zahl1!s}")
print(f"{text!a}")
print(f"{zahl1:0>12b}\n{zahl2:g}")
# !a => Konvertiert variable in ascii
# !s => Konvertiert zum string (ruft intern die __str__ Methode des Objekts auf)
# !r => __repr__ Methode auf ! Seltener Fall
# {variable(!a):anordnung padding typ .präzision>}
# Anordnung: < Links bündig, ^ zentriert, > rechtsbündig
# typ: b - binär, i - integer, g-Kommazahl, G -Exponential, % - Prozentual, x - Hexadezimal, d - dezimal, o - Oktal
# padding: Anzahl Stellen insgesamt
# präzision: Genauigkeit der Zahl, z.B. Trennen von Kommastellen

# Input:

# name = input("Wie ist dein Name?\n") # In den Klammern wir der Text spezifiziert
# print(f"Hallo {name}")
#
# # Standarmäßig ist der input immer ein String
# # Wenn wir den Typen verändern wollen müssen wir ihn casten
#
# print("Wir rechnen jetzt x + y")
# x = float(input("Gib einen Wert für x ein:\n"))
# y = float(input("Gib einen Wert für y ein:\n"))

# print(f"{x} + {y} = {x+y}")

# open()
# Ermöglicht es uns Dateien zu öffnen
# open(Pfad, Modus)
# Modi:
# r - read, kann nur lesen und ist auch der Standardwert
# w - write, kann schreiben und falls die Datei nicht exisitert, wird sie neu erstellt
# a - append, hängt an eine bestehende Datei etwas an
# w+/r+ - read&write kann sowohl lesen als auch schreiben, falls Datei nicht existiert wird sie erstellt

# file = open("test.txt", "w+")
# textInput = input("Was willst du in die Datei schreiben?\n")
# textInput += "\n"
# file.write(textInput) # write fügt den Text an
# newLines = ["test1\n", "test2\n", "test\n"]
# file.writelines(newLines)
# file.close() # close ist wichtig, da ohne das close nichts gespeichert wird
#
# file = open("test.txt", "r")
# for line in file:
#     print(line)
# file.close()

# Alternative zu close()

with open("test2.txt", "w+") as newFile:
    print("Anfange des Blocks")
    for i in range(1,101):
        newFile.write(f"Zeile {i} \n")

print("Ende des Blocks")

# csv für CSV Dateien
# PIL Python Imaging Library für Bilder
# json für json Dateien
# os für Interaktion mit dem betriebssystem

# Das os-Modul an
# Ist ein Modul, muss also importiert werden

print(os.listdir())


if not os.path.exists("text"):
    os.mkdir("text")

# state = True
#
# while state:
#     name = input("Wie soll die Datei heißen?")
#     name += ".txt"
#     path = "text/"
#     path += name
#     operation = input("Welche operation soll durchgeführt werden?\nw+\nr\na\n")
#     if operation == "w+":
#         if os.path.exists(path):
#             print("Fehler! Datei existiert bereits")
#         else:
#             with open(path, operation) as newFile:
#                 line = input("Was soll geschrieben werden?\n")
#                 newFile.write(line)
#                 state = False
#     elif operation == "a":
#         if  not os.path.exists(path):
#             print("Fehler! Datei nicht gefunden")
#         else:
#             with open(path, operation) as newFile:
#                 line = "\n"
#                 line += input("Was soll geschrieben werden?\n")
#                 newFile.write(line)
#                 state = False
#     elif operation == "r":
#         with open(path, operation) as newFile:
#             for line in newFile:
#                 print(line)
#             state = False

# 1. Übung:
# Wollen wir eine Schleife bauen, die über die ersten 40 Zahlen iteriert von 1 - 40
# Jedes mal wenn eine Gerade Zahl vorkommt soll in der Konsole gerade ausgegebn werden
# Das Programm soll vorher in der Konsole fragen bis zu welcher Zahl gezählt werden soll

# 2. Übung
# Wir wollen, dass das Programm den User nach einem Dateinamen fragt und falls die Datei noch nicht exisitert soll
# sie erstellt werden und danach kann der User einen Text eingeben der in die datei geschrieben wird
# Falls die Datei bereits existiert soll der Text angehängt werden

print(f"Der Name des Scripts/Programms: {s.argv[0]}")
for args in  s.argv:
    print(args)

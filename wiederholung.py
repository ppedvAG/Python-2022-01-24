import os
# Kontrollstrukturen
# Welche gibt es?
# if, elif, else ternären Operator
# while
# for
# match...case

# Übung:
# Wollen wir eine Schleife bauen, die über die ersten 40 Zahlen iteriert von 1 - 40
# Jedes mal wenn eine Gerade Zahl vorkommt soll in der Konsole gerade ausgegebn werden

border = int(input("Bis zu welcher Zahl sollg ezählt werden?"))

for i in range(1,border +1 ,1):
    if i % 2== 0:
        print("Gerade")


name = input("Wie heißt die Datei?")
name += "txt"

if os.path.exists(name):
    with open(name, "a") as file:
        print("Datei exisitert beretis.\nText wird angehängt")
        newText = "\n"
        newText += input("Was soll geschrieben werden?")
        file.write(newText)
else:
    with open(name, "w+") as newFile:
        print(f"{name} wurde erstellt.")
        newText = input("Was soll geschrieben werden?")
        file.write(newText)
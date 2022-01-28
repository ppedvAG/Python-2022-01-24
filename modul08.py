# Lambda Funktionen / Anonyme Funktionen
# Pfeilfunktionen
import sqlite3 as sql

lambdaTest = lambda x, y: x + y
print(lambdaTest(4, 8))

# Statt def nehmen wir lambda
# brauchen kein Return
# brauchen an sich keinen Funktionsnamen (aber eine Variable)
# Parameter sind nicht von einer Klammer umschlossen
# Ansonsten wie normale Funktionen

# Vorteil: meist kürzer
# Nachteil: Unleserlicher und nicht so klar definiert
# Werden gerne als Parameter übergeben:
# map(), filter()
myList = list(range(1001))


def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

# myNewList = filter(lambda x: x % 13 == 0, myList)


myNewList = list(filter(isEven, myList))
# die Lambda expresssion muss in diesem Fall true oder false ergeben, damit die Liste dementsprechend gefiltert werden
# kann
print(list(myNewList))
myNewList = list(map(lambda x: x*x, myNewList))

print(myNewList)

# Immediatly Invoked Function
(lambda x, y : print(f"{x}+{y} = {x+y}"))(12, 2)
# Sind einmalig, da sie keinen Namen haben, haben auch keine Referenz
# Es wird von der Verwendung abgeraten
# Und sie müssen immer von runden Klammern umgeben sein

# Lambda als Ausdruck:


def normaleFunc(x):
    return lambda y: y * x


verdoppler = normaleFunc(2)

print(verdoppler)
print(verdoppler(12))


# Höhere Funktionen:
# Eine Funktion nennt man dann höhere Funktion, wenn einer ihrere Parameter
# eine Referenz auf eine andere Funktion ist/ lambda

# map(lambda/callback, iterierbares Objekt z.B. ne Liste)
# DIe map Funktion iteriert über die Liste und wendet auf jedes Element die lambda/callback funktion an
# Rückgabe ist ein map-Objekt => wir müssen es erst Casten falls wir wieder eine Liste haben wollen

# filter(lambda/callback, iterierbares Objekt)
# Iteriert auch über jedes Element prüft ob beim callback/lambda true rauskommt, falls ja wird es zum filter-Object
# hinzugefügt
# Falls nein wirds übersprungen
# AUch hier casten!

# Übung:
# testList = list(range(51))
# Nutze die filter-Funktion um nur Vielfache von 17 in eine neue Liste zu geben
# Lasse die neue Liste anschließend in der Konsole ausgeben

# TODO: Datenbankenverbindung, Fehlerbehandlung, GUI, Tests, scipy
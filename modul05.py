import time

# Funktionen
# Funktionen sind Objekte erster Klasse
# d.h. wir können sie Variablen zuweisen, wir können sie anderen Funktionen übergeben und wir können sie sogar
# von anderen Funktionen zurückgeben lassen


def meineErsteFunktion():
    print("Ich bin eine Funktion.")


mef = meineErsteFunktion

meineErsteFunktion()
mef()


def greeter(name):
    print(f"Hallo {name}")
    global mef # Mit dem global Keyword können wir das Verwenden einer globalen Variable erzwingen
    mef()

    def mef():  # #Funktionen können verschachtelt werden
        print("Ich bin eine innere Funktion")
    mef()
    variableX = 12
    print(variableX)


# Scope in Python:
# Er schaut erst ob es eine built-in Funktion gibt mit dem Namen
# Es wird erst im lokalen Scope gesucht
# Als letztes wird im globalen Scope nachgeschaut


greeter("Max Mustermann")


# print(variableX) Geht nicht, da variableX nur in der Funktion greeter bekannt ist

# Wir können mit Funktionen auch werte zurückgeben


def summe(intOne, intTwo):
    return intOne + intTwo


x = 55
y = 79
z = summe(x, y)
print(z)

# Wie dokumentieren wir unsere Funktionen


def subtraktion(intOne:int, intTwo:int) -> int:  # Type Annotation → Erzwingt aber nicht den richtigen Typen
    # Ist mehr ein Vorschlag
    """
    Eine Funktion, die zwei Zahlen voneienander abzieht und das Ergebnis ausgibt.
    :param intOne: Zahl von der subtrahiert wird
    :param intTwo: Zahl die von intOne abgezogen wird
    :return: Differenz der beiden Zahlen
    """
    if type(intOne) != int or type(intTwo) != int:
        print("Es werden nur integer akzeptiert")
        return 0
    return intOne - intTwo


# print(subtraktion("as", "dsa"))


# Rekursive Funktionen:
# Prinzipiell nur eine Funktion, die sich in ihrem Körper selber aufruft

def factorialR(zahl: int) -> int:
    """
    Gibt die Fakultät der eingegeben Zahl zurück
    :param zahl: Zahl, deren Fakultät berechnet werden soll
    :return: Ergebnis der Berechnung
    """

    if zahl == 1 or zahl == 0:
        return 1
    else:
        return zahl * factorialR(zahl - 1)


start = time.time()
print("Messung Beginnt")
print(factorialR(998))
end = time.time()
print(f"Vergangen Zeit: {end - start}")


def factorialL(zahl: int) -> int:
    result = 1
    for i in range(zahl, 0, -1):
        result *= i
    return result


start = time.time()
print("Messung Beginnt")
print(factorialL(998))
end = time.time()
print(f"Vergangen Zeit: {end - start}")

# Verschiedene Parameter Arten in Python:

# Positional, d.h. sie werden der Reihe nach übergeben

summe(4, 5)  # die erste Zahl ist intOne und die zweite Zahl ist intTwo

# Keyword Argument

print(summe(intTwo=4, intOne=8))

# Wir können bei den Keywords bestimmen welcher Parameter wie befüllt wird
# Syntax parameterName=Wert

# Arbitrary Arguments

# summe(4, 5, 6)  Funktioniert nicht, da zu viele Parameter übergeben wurden


def summeAr(*numbers: int):
    result = 0
    for integer in numbers:
        result += integer
    print(result)
    return result

# Arbitrary Arguments erlauben die Übergabe beliebig vieler Parameter
# Python packt dann alle übergebenen Werte in ein Tupel
# d.h. wir müssen über das Tupel iterieren
# In den Python docs *args betitelt


wert = summeAr(1, 2, 6, 12, 11, 49, 7)


# Arbitrary Keyword Arguments
# Die Arbitrary KEywords werden in ein Dicitonary umgewandelt


def arbKeyWords(**words):
    for key in words:
        print(words[key])


def keyValue(**dict):
    for key, value in dict.items():
        print(f"Key: {key}, value: {value}")


arbKeyWords(zahl1=12, zahl2=23)

# Dictionary: words = {
# "zahl1": 12,
# "zahl2: 23
# }

keyValue(vorname="Marius", nachname="Sommer", alter=26, geschlecht="Männlich")

# Mit arbitrary Keywords kann ich beliebig viele benannte Parameter übergeben
# In den Python Docs werden die arbitrary Keywords als **kwargs betitelt

myTuple = (1, 2, 5, 6)


# summeAr(myTuple) Klappt nicht, da das Tupel als ein Parameter übergeben wird und ((1,2,5,6))

summeAr(*myTuple) # unpacking, er packt mein Tupel aus und
# summeAr(1,2,5,6) so sieht es ausgepackt aus

marius = {
    "vorname": "Marius",
    "nachname": "Sommer",
    "alter": 26,
    "geschlecht": "männlich"
}


keyValue(**marius)  # Unpacking Operator bei Dictionaries


def showDict(dict: dict):
    for key in dict:
        print(f"Key: {key}, value: {dict[key]}")


showDict(marius)

# Default Parameter:

# WIr können einen Default Wert angeben, der benutzt wird, falls der Parameter nicht befüllt wird
# Default Parameter müssen immer nach den Positional/Keywordatguments angegeben werden
def divide(intOne=1, intTwo=1):
    if intTwo == 0:
        intTwo = 1
    return intOne / intTwo


print(divide())

# Parameter Reihenfolge:
# 1. Positionals/Keywords
# 2. Default-Parameter
# 3. Arbitrary Arguments können Platz mit 2. tauschen
# 4. Arbitrary Keywords  müssen als letztes stehen


def multipliaktion(intOne, /, *, intTwo):  # intOne kann jetzt nur noch als positional übergeben werden und intTwo
    # nur als Keyword
    return  intOne * intTwo

# Merke: nach Parametern, die nur als positionals, übergeben werden dürfen setzen wir einen /
# Merke: Vor Parametern, die nur als Keyword, übergeben werden dürfen setzen wir ein *


print(multipliaktion(4, intTwo=6))


# Decorator:


def sayHello(function):
    print("Hallo")
    function()


# sayHello(meineErsteFunktion)  # WIr übergeben eine Referenz auf die Funktion, ein sogenannter Callback


def greetMax(function):
    return function("Max")


# greetMax(greeter)


def doppelt(func):
    def wrapper():
        print("Ich werde davor ausgeführt")
        func()
        func()
        print("Ich werde danach ausgeführt")
    return wrapper


meineZweiteFunktion = doppelt(meineErsteFunktion)
meineZweiteFunktion()


@doppelt
def gibUhrzeit():
    print(time.time())


def timeFunction(func):
    def wrapper():
        start = time.time()
        print(f"Start der Ausführung: {start}")
        func()
        end = time.time()
        print(f"Dauer: {end - start}")
    return wrapper

# Bei Decoratoren wird immer mit einem Wrapper kombiniert, der zurückgegeben wird

@timeFunction
def zaehlLange():
    for i in range(10):
        print(i)


# gibUhrzeit()

# Decorators benutze ich wenn ich Funktionalität vor einer Funktion dazupacken will

zaehlLange()


def logger(func):
    def wrapper():
        print(f"{func} wird ausgeführt.")
        func()
        print(f"Ausführung von {func} beendet.")
    return wrapper


# Reihenfolge ist für die Benennung wichtig, da sonst eventuell der falsche FFunktionsname wiedergegeben wird
@timeFunction
@logger
def zaehlLaenger():
    for i in range(100000):
        print(i)


zaehlLaenger()

vorname = "Marius" # Variable definieren
mittelname = "Gabriel"
nachname = "Sommer"
print("Hallo Welt")
print("Hallo " + vorname + " " + mittelname + " " + nachname + ", heute ist ein schöner Tag") # Hängt String hinten an
# formatted String
print(f"Hallo {vorname} {mittelname} {nachname}, heute ist ein schöner Tag") # Fügt name direkt in den Text ein

# Typen:
# Primitive:
text = "Ich bin eine Text variable" # Type: str
integer = 12 # int
double = 12.444 # float
complexe = 12 + 2j
bool = True # boolean

# Listenähnliche:
# dict Dictionary
# list Liste
# tuple
# range
# set

# String:
name = "Max Mustermann"
# Slicing:
# name[startposition:endposition(Nicht inklusive):Schrittgröße]

# Methoden:
name.count("x") # WIe oft kommt x vor?, Falls nicht vorhanden 0
name.index("n") # Index des ersten vorkommens, ist case-sensitive!

name.isalpha() # Nur Buchstaben
name.isnumeric() # Nur Zahlen
name.isalnum() # Zahlen oder Buchstaben

name.title() # Gibt neuen String zurück, bei dem jeder WOrtanfang groß geschrieben ist
name.capitalize() # Gibt neuen String zurück, bei dem der Angangsbuchstabe des ersten Wortes groß geschrieben ist

name.lower() # Alles kleingeschrieben
name.upper() # ALles großgeschrieben

name.lstrip() # Entfernt ohne Parameter überhängende Leerzeichen auf der linken Seite
name.rstrip() # Entfernt ohne Parameter überhängende Leerzeichen auf der rechten Seite

# Mit Parametern wird der entsprechende Buchstabe entfernt

name.split() # Trennt den STring ohne Parameter bei Leerzeichen mit Parameter anhand des Parameters
name.replace("Max", "Maximilian") # Gibt neuen String zurück der Parameter 1 mit Parameter 2 ersetzt

# Zahlen:
# Operatoren:
# + Addition
# - Subtraktion
# * Multiplikation
# / Divison
# % Modulus
# ** Potenz
# // Ganzahl-Division

## Logische Operatoren

# and - Und
# or - oder
# not - Verneint
# is - Prüft ob identisch, anhand einer ID
# is not - Nicht identisch, anhand einer ID
# in - ist enthalten
# not in - nicht enthalten

# Vergleiche:

# == Vergleicht werte
# != Ungleiche Werte

## Liste:
# Reihenfolge steht fest, kann über auf einzelen WErte zugreifen
# Kann die Liste verändern
myList = ["Kann", 123124124, True, "verschiedene Typen enhalten", [12, 123,545, True]]
# Können wie bei Strings das Slicing benutzen

# Methoden der Listen:

myList.append(123) # Fügt 123 ans Ende der Liste an
myList.clear() # leert die Liste
myList.copy() # Gibt eine identische Kopie der Liste zurück
myList.count(12) # Wie oft kommt das Element in der Liste vor?
myList.extend(myList) # Hängt ein iterierbares Objekt an die Liste an
#myList.index(12) # Gibt an an welcher Position das gesuchte Element steht
myList.insert(0, "Test")  # Fügt an der angegebenen Position den übergebenen Wert ein
## len() EIngebaiute FUunktion um die Länge von Objekten zu Prüfen
myList.pop(0) # Entfernt das Element am angegebenen Index und gibt den Wert zurück, Ohne Parameter entfernt er das letzte ELement
myList.append(15)
myList.remove(15) # Entfernt das Element mit dem Wert 15
myList.reverse() # Kehrt die Reihenfolge der Liste um
myList.sort() # Sortier die Liste standardmäßig Alphanumerisch aufsteigend

# Tuple:
# Sind geordnet, d.h. sie haben einen Index
# Sie sind nicht veränderbar, können keine neuen Elemente hinzufügen oder bestehende entfernen

myTuple = (1, 2, 3, 4)

# Methoden
myTuple.count(1) # Wie oft kommt das element vor?
myTuple.index(1) # An welcher Stelle steht das Element?

# Kombination von Tupeln:

myTuple2 = (5,6,7,8)
myTuple3 = myTuple + myTuple2
print(myTuple3)

# Range
# Nichtveränderbare Sequenz von Integern
range(101) # Zahlen von 0 bis 100 Enzahl ist nicht inklusive
range(10, 101, 10) # Er fängt bei 10 (Startzahl ist inklusive), Hört bei 100, zählt in 10er Schritten

# Dictionaries:

# Sind geordnet
# Enthalten Key: Value Paare
# Können neue ELemente hinzufügen, entfernen, und bestehende Ändern
# Keine DUplikate bei den Keys

meinAuto = {
    "Marke": "BMW",
    "Modell": "i3",
    "Baujahr": 2020
}

# Methoden:

meinAuto.copy() # GIbt uns eine Kopie des Elementes zurück
meinAuto.get("Marke") # Gibt Wert des KEys zurück => Eig Identisch wie meinAuto["Marke"]
meinAuto.items() # GIbt alle Key-Value Paare als Tupel zurück
meinAuto.keys() # Gibt alle Keys als Liste zurück
meinAuto.pop("Baujahr") # Entfernt angegebenes Key-Value Paar
meinAuto.popitem() # Entfernt das letzte Key-Value Paar des Objekts
meinAuto.values() #Gibt  Liste mit allen Werten zurück
meinAuto.update("Marke", "Audi") # Weist dem Key einen neuen Wert zu
meinAuto.setdefault("Marke", "Tesla") # Falls der Key exisitiert, gibt die Funktion den Wert zurück
# Falls der Key noch nicht exisitert wird erstellt und der zweite Parameter wird als Wert genommen
meinAuto.clear() # Entfernt alle Keys und Values

# Sets
# Sind nicht geordnet => Kein Index
# Können neue Werte hinzufügen, wir können welche entfernen, aber bestehende Werte können nicht geändert werden
# Duplikate sind nicht erlaubt

mySet = {1, 2, 2, 3, 4}

# Set Methoden:

mySet.add(12) # Neues Element wird hinzugefügt
mySet.copy() # Gint eine Kopie des Sets zurück
mySet.difference(myTuple) # Gibt die Elemente aus dem Set zurück, die nicht in dem Parameter enthalten sind
# mySet.difference_update(myTuple) # Entfernt die Elemente aus dem Set, die auch im Parameter enthalten sind
mySet.discard(4) # Entfernt das angegebene Element aus dem Set
mySet.intersection(myTuple) # Gibt ein Set zurück, das nur aus gemeinsamen Elementen besteht
mySet.intersection_update(myTuple) # Entfern alle Elemente aus dem Set, die nicht im Parameter enthalten sind
mySet.isdisjoint(myTuple) # Prüft ob keins der Elemente vom Set in dem Parameter enthalten sind, falls keine Gemeinsamkeiten bestehen => True,
# ansonsten False
mySet.issubset(myTuple) # Ist das aufrufende Set komplett in dem Parameter-Set enthalten
mySet.issuperset(myTuple) # Ist das Parameter-Set komplett im aufrufendne Set enthalten
mySet.pop() # Entfern das erste Element des Sets
mySet.remove(1) # Entfernt angegebenes Element aus dem Set, Fehler falls nicht vorhanden
mySet.union(myTuple) # gibt ein Set zurück, das die angegebenen Sets kombiniert
mySet.update(myTuple) # Fügt noch nicht vorhandenen Elemente aus dem Parameter in das Set ein
mySet.clear() # Set wird geleert


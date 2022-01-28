# Kontrollstrukutren

# if -Anweisung

if 2 > 1: # Hier wird Bedingung geprüft
    print("2 ist größer als 1.") # Wird nur ausgeführt falls die Bedingung war ist


intOne = 10
intTwo = 5

if intOne < intTwo:
    print(f"{intOne} ist kleiner als {intTwo}.")
    if intOne % 2 == 0:
        print(f"{intOne} ist gerade")
elif intOne < intTwo:
    print(f"{intOne} ist größer als {intTwo}.")
else:
    print("Die Zahlen sind gleich groß.")


intThree = 11
intFour = 15

if intThree < intFour: print("IntThree ist kleiner")

# Ternär Operator:

print("intThree ist größer als intFour") if intThree > intFour else print("intThree und intFour sind gleich groß") if intThree == intFour else print("IntThree ist kleiner als intFour")

if intOne < intFour:
    print("halo")
intOne = 7

if intOne:
    print(f"{intOne}")
else:
    print("intOne ist nicht True")

# Match-case: switch-case der anderen Sprachen

match intOne:
    case 10 | 7:
        print("intOne ist 10 oder 7")
    case 5:
        print("intOne ist 5")
    case _:
        print("IntOne ist weder 10 noch 5")

bspList = [1,2,3,4, 6]

match bspList:
    case 1:
        print("List ist 1 bis 4")
    case _ if len(bspList) > 4: # Können mit if kombiniert werden, guard
        print("Die List ist lang")
    case _:
        print("Die Liste ist kurz")

# Die Schleifen:
# In Pyhton gibt es prinzipiell nur Kopfgesteuerte Schleifen

# while-SChleife:

i = 0

while i < 101:
    print(i)
    i += 10
else: # Kann mit Else verknüpft werden
    print(f"i ist nicht mehr kleienr als 100. Wert i: {i}")

i = 46
while True:
    print(i)
    i += 1
    if i > 46:
        break

# Fußgesteurte Schleife:
# Endlos Schleife bauen und mit if kombinieren um Endbedingung einzubauen
# Ohne if block läuft sie endlos

# For Schleife:

myDict = {
    "TestAttr": 1,
    "TestZwei": "Hallo"
}

for value in bspList:
    print(value)

for item in myDict:
    print(myDict[item])

nestedList = [[1,2,3], [4,5,6], [7,8,9]]

for list in nestedList:
    print(list)
    for element in list:
        print(element)

for i in range(10,101,10):
    print(i)





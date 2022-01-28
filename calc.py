import sys
from try_parse.utils import ParseUtils
arg = sys.argv
operators = ["a", "s"]
if len(arg) == 1:
    print("Es muss genau ein Parameter übergeben werden")
    exit(-1)
elif arg[1] not in operators:
    print(f"{arg[1]} ist ein ungültiger Parameter. Bitte wählen sie a oder s")
else:
    intOne = ParseUtils.try_parse_int(input("Zahl1: "))
    while not intOne[0]:
        intOne = ParseUtils.try_parse_int(input("Bitte gib einen gültigen Integer ein: "))
    intOne = intOne[1]
    intTwo = ParseUtils.try_parse_int(input("Zahl2: "))
    while not intTwo[0]:
        intTwo = ParseUtils.try_parse_int(input("Bitte gib einen gültigen Integer ein: "))
    intTwo = intTwo[1]
    if arg[1] == "a":
        print("Sie haben Addition gewählt.")
        print(f"{intOne} + {intTwo} = {intOne + intTwo}")
    elif arg[1] == "s":
        print("Sie haben Subtraktion gewählt.")
        print(f"{intOne} - {intTwo} = {intOne - intTwo}")
    # Einen zweiten elif Block schreiben, der sich um die Subtraktion kümmert

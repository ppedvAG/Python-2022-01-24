# Module
# Grundlegend sind Module Code Bibliotheken, die wir importieren können
# Sie stellen uns neue Funktionalitäten zur Verfügung, die in ihnen definiert wurden
# Jede Python Datei ist an sich ein Modul, Dateiname entspricht dem Modul Namen

# __name__ = "TestName" Kann Namen erzwingen

import modul06 as m6  # Alias
import helper.mathOps as mo
from personen import *

# Erleichtert die Strukturierung, da wir Klassen oder Funktionen auslagern können

lessie = m6.Collie(8, "Lessie", "Beige", 3)

lessie.retteKind()

print(__name__) # Gibt den Namen des Moduls aus

# Falls es sich dabei um das gerade ausgeführte Modul handelt wird der Name auf __main__ gesetzt


def main():
    print("Modul7 wird getestet")
    lessie.retteKind()
    print(lessie)
    x = mo.subtrahieren(6, 5)
    y = mo.summieren(12, 55)
    print(x)
    print(y)
    p1 = Kunde.Kunde()
    print(p1.alter)


if __name__ == "__main__":
    main()


# Die Module müssen nicht unbedingt in Python verfasst sein
# Wir können Module auch in C schreiben

# Vorteile:
# Aufbrechen in Teile
# Wartbarkeit
# Wiederverwendbarkeit
# Gültigkeit: Funktionen können mehrfach existieren, da wir prefixes benutzen

# m5.summe(5, 5)
m6.summe(7, 8)

# Modul Suchpfad:
# Python prüft ob es ein integriertes Modul ist, aufpassen bei der Benennung und keine integrierten Modulnamen verwenden
# z.B. os
# Schaut im eigenen Ordner ob ein Modul mit dem Namen existiert
# PYTHONPATH-Variable, Ort der Pythoninstallation im Falle von Pycharm also immer das virtual Environment
# Falls es da auch nicht gefunden wird => Fehler


# Erstelle ein neues Modul, das Modul soll zwei Funktionen enthalten, die division und multiplikation bieten
# Erstelle eine Datei namens lab07.py die in ihrer Main Funktion die beiden importierern Funktionen benutzt und
# das Ergebnis in der Konsole ausgibt

